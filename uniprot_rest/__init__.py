from __future__ import annotations

import dataclasses
from dataclasses import dataclass
import gzip
from typing import TYPE_CHECKING, Any, Iterable, Mapping, TextIO, TypeVar
from typing_extensions import Self, TypeAlias, TypedDict

from uniprot_rest.dataset import Dataset
from uniprot_rest.format import Format

import requests

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element

def lookup(id: str, dataset: Dataset, format: Format) -> requests.Response:
    return requests.get(f"https://www.uniprot.org/{dataset}/{id}.{format}")


@dataclasses.dataclass
class SearchRequest:
    high_level: Search
    compressed: bool = True
    cursor: str | None = None

    def params(self) -> dict[str, str]:
        """
        :return:
        """
        params = dataclasses.asdict(self)
        params.pop("high_level")
        return {**params, **self.high_level.params()}

    def to_request(self) -> requests.PreparedRequest:
        return requests.Request(
            method="GET",
            url=f"https://rest.uniprot.org/{self.high_level.dataset}/search",
            params=self.params()
        ).prepare()


def unzip_response(response: requests.Response) -> str:
    return gzip.decompress(response.raw).decode()

# class JsonResults(TypedDict):
#     pass

# class JsonRecord(TypedDict):
#     results: JsonResults
def serialize_query(query: Mapping[str, Any], level: int = 0) -> str:
    if len(query) > 1:
        # If we ever find a dictionary with more than one key, we treat it as an AND
        return serialize_query({
            "and": [{key: value} for key, value in query.items()]
        })
    key, value = next(iter(query.items()))
    if key == "and":
        ret = " AND ".join([
            serialize_query(it, level=level+1) for it in value
        ])
    elif key == "or":
        ret = " OR ".join([
            serialize_query(it, level=level+1) for it in value
        ])
    elif key == "not":
        ret = f"NOT {serialize_query(value, level=level+1)}"
    else:
        return f"{key}:{value}"
    
    if level > 0:
        return f"({ret})"
    else:
        return ret





DatasetType = TypeVar("DatasetType")
QueryType = TypeVar("QueryType")
FieldType = TypeVar("FieldType")

class JsonRecord(TypedDict, total=False):
    primaryAccession: str

# Query: TypeAlias = TypedDict("Query", {
#     "and": QueryType,
#     "or": QueryType
# })
# class Query(TypedDict, total=False):
#     and: Self
#     or: Self

@dataclass
class Search:
    query: str | Mapping[str, Any]
    dataset: Dataset = "uniprotkb"
    format: Format = "json"
    fields: Iterable[str] | None = None
    include_isoform: bool = True
    size: int = 500

    def params(self) -> dict[str, str]:
        """
        Returns the URL query parameters that can be derived from this object
        """
        # return {
        #     query = 
        # }
        params = dataclasses.asdict(self)
        if self.fields:
            params["fields"] = ",".join(self.fields)
        params.pop("dataset")
        return params

    def each_page(self) -> Iterable[TextIO]:
        session = requests.Session()
        request = SearchRequest(self).to_request()
        while True:
            response = session.send(request, stream=True)
            yield gzip.open(response.raw, mode="rt", encoding=response.encoding)
            link: dict[str, Any] | None = response.links.get("next")
            if link is not None:
                # pyright: ignore
                request = requests.Request("GET", link["url"]).prepare()
            else:
                break

    def each_record(self):
        if parser := getattr(self, f"each_{self.format}", None):
            for page in self.each_page():
                yield from parser(page)
        else:
            raise NotImplementedError(f'No parser is implemented for the "{self.format}" format.')
        # "html", "txt", "xml", "rdf", "fasta", "gff", "json", "list", "tsv", "obo", "xlsx"

    @staticmethod
    def each_json(page: TextIO) -> Iterable[JsonRecord]:
        import json
        parsed = json.load(page)
        yield from parsed["results"]

    @staticmethod
    def each_tsv(page: TextIO) -> Iterable[dict[str, str]]:
        import csv
        reader = csv.DictReader(page, delimiter="\t")
        yield from reader

    @staticmethod
    def each_xml(page: TextIO) -> Iterable[Element]:
        from xml.etree import ElementTree
        tree = ElementTree.parse(page)
        yield from tree.getroot().findall("{*}entry")

    @staticmethod
    def each_list(page: TextIO) -> Iterable[str]:
        yield from page.read().splitlines()

