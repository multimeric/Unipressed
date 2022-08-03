from __future__ import annotations

import dataclasses
import datetime
import gzip
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Iterable, Mapping, TextIO, Union, overload

import requests
from typing_extensions import TypedDict

from unipressed.dataset import Dataset
from unipressed.format import Format

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element


@dataclasses.dataclass
class SearchRequest:
    """
    Low level options for a Uniprot request, which the user generally doesn't need to consider
    """

    high_level: Search
    compressed: bool = True
    cursor: str | None = None

    def params(self) -> dict[str, str]:
        """
        :return:
        """
        params = dataclasses.asdict(self)
        params.pop("high_level")
        return {**params, **self.high_level._params()}

    def to_request(self) -> requests.PreparedRequest:
        return requests.Request(
            method="GET",
            url=f"https://rest.uniprot.org/{self.high_level.dataset}/search",
            params=self.params(),
        ).prepare()


def serialize_query(query: Any, level: int = 0) -> str:
    """
    Recursively converts a query object into a Uniprot query string

    Args:
        query (Any): A dict, str, or any other type to convert to string
        level (int, optional): The current depth into the query
    """
    if isinstance(query, dict):
        if len(query) > 1:
            # If we ever find a dictionary with more than one key, we treat it as an AND
            return serialize_query(
                {"and_": [{key: value} for key, value in query.items()]}
            )
        key, value = next(iter(query.items()))
        if key == "and_":
            ret = " AND ".join([serialize_query(it, level=level + 1) for it in value])
        elif key == "or_":
            ret = " OR ".join([serialize_query(it, level=level + 1) for it in value])
        elif key == "not_":
            ret = f"NOT {serialize_query(value, level=level+1)}"
        else:
            return f"{key}:{serialize_query(value)}"

        if level > 0:
            return f"({ret})"
        else:
            return ret
    elif isinstance(query, tuple) and len(query) == 2:
        a, b = query
        return f"[{serialize_query(a)} TO {serialize_query(b)}]"
    elif isinstance(query, datetime.date):
        return query.strftime("%Y-%m-%d")
    elif isinstance(query, bool):
        return str(query).lower()
    else:
        return str(query)


class JsonRecord(TypedDict, total=False):
    primaryAccession: str


@dataclass
class Search:
    """
    Base class for all search requests.
    """

    query: Union[str, Mapping[str, Any]]
    "A query that filters the returned proteins. Either a string if you have an existing query and want to bypass the type checker, or a dict if you want code completion and validation."
    dataset: Dataset = "uniprotkb"
    """
    The Uniprot database. You are advised to use the appropriate subclass (e.g. [unipressed.UniprotkbSearch][] where available.
    """
    format: Format = "json"
    "Format for the returned data. Defaults to `'json'`."
    fields: Union[Iterable[str], None] = None
    "An iterable of fields to return in the result object."
    include_isoform: bool = True
    "For uniprotkb only: if `True`, returns isoforms other than just the canonical isoform."
    size: int = 500
    "The size of each page. Changing this may slightly affect performance, and you aren't recommended to do so unless you have a reason to."

    def _params(self) -> dict[str, str]:
        """
        Returns the URL query parameters that can be derived from this object
        """
        ret = {
            "query": serialize_query(self.query),
            "dataset": self.dataset,
            "format": self.format,
            "includeIsoform": str(self.include_isoform).lower(),
            "size": str(self.size),
        }
        if self.fields:
            ret["fields"] = ",".join(self.fields)
        return ret

    def each_response(self) -> Iterable[requests.Response]:
        """
        Returns a generator of [`requsets.Response`](https://requests.readthedocs.io/en/latest/api/#requests.Response) objects, one for each page of the result
        """
        session = requests.Session()
        request = SearchRequest(self).to_request()
        while True:
            response = session.send(request, stream=True)
            yield response
            link: dict[str, Any] | None = response.links.get("next")
            if link is not None:
                # pyright: ignore
                request = requests.Request("GET", link["url"]).prepare()
            else:
                break

    def each_page(self) -> Iterable[TextIO]:
        """
        Returns a generator of unzipped [file objects](https://docs.python.org/3/library/io.html#io.TextIOBase), one for each page of the result
        """
        for response in self.each_response():
            yield gzip.open(response.raw, mode="rt", encoding=response.encoding)

    def each_record(self) -> Any:
        """
        Returns a generator of records, which are defined by the format field of the original request.
        For example, with `format="json"`, this will be an iterator over dictionaries parsed from JSON.
        """
        parser = getattr(self, f"_each_{self.format}", None)
        if parser is not None:
            for page in self.each_page():
                yield from parser(page)
        else:
            raise NotImplementedError(
                f'No parser is implemented for the "{self.format}" format.'
            )

    @staticmethod
    def _each_json(page: TextIO) -> Iterable[JsonRecord]:
        import json

        parsed = json.load(page)
        yield from parsed["results"]

    @staticmethod
    def _each_tsv(page: TextIO) -> Iterable[dict[str, str]]:
        import csv

        reader = csv.DictReader(page, delimiter="\t")
        yield from reader

    @staticmethod
    def _each_xml(page: TextIO) -> Iterable[Element]:
        from xml.etree import ElementTree

        tree = ElementTree.parse(page)
        yield from tree.getroot().findall("{http://uniprot.org/uniprot}entry")

    @staticmethod
    def _each_list(page: TextIO) -> Iterable[str]:
        yield from page.read().splitlines()
