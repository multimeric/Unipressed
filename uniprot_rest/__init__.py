from __future__ import annotations

import dataclasses
from dataclasses import dataclass
import gzip
from typing import Literal, Iterable, TypedDict, TextIO

import requests

def lookup(id: str, dataset: Dataset, format: Format) -> requests.Response:
    return requests.get(f"https://www.uniprot.org/{dataset}/{id}.{format}")


@dataclasses.dataclass
class SearchRequest:
    high_level: Search
    compressed: bool = True
    cursor: str | None = None

    def params(self) -> dict:
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

class JsonResults(TypedDict):
    pass

class JsonRecord(TypedDict):
    results: JsonResults

@dataclass
class Search:
    query: str
    dataset: Dataset
    format: Format = "json"
    fields: Iterable[Field] | None = None
    include_isoform: bool = True
    size: int = 500

    def params(self) -> dict:
        """
        Returns the URL query parameters that can be derived from this object
        """
        params = dataclasses.asdict(self)
        params["fields"] = ",".join(params.get("fields"))
        params.pop("dataset")
        return params

    def each_page(self) -> Iterable[TextIO]:
        session = requests.Session()
        request = SearchRequest(self).to_request()
        while True:
            response = session.send(request, stream=True)
            yield gzip.open(response.raw, mode="rt", encoding=response.encoding)
            if link := response.links.get("next"):
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
    def each_json(page: TextIO) -> Iterable[TypedDict('JsonRecord', {'primaryAccession': str}, total=False)]:
        import json
        parsed = json.load(page)
        yield from parsed["results"]

    @staticmethod
    def each_tsv(page: TextIO) -> dict:
        import csv
        reader = csv.DictReader(page, delimiter="\t")
        yield from reader

    @staticmethod
    def each_xml(page: TextIO) -> dict:
        from xml.etree import ElementTree
        tree = ElementTree.parse(page)
        yield from tree.getroot().findall("{*}entry")

    @staticmethod
    def each_list(page: TextIO) -> Iterable[str]:
        yield from page.read().splitlines()



# class KbQuery:
#     pass
#
#
# class Search(BaseModel):
#     """
#     Kwargs common to any UniProt search
#     """
#     query: str
#     dataset: Dataset
#     format: Format
#     fields: Iterable[str]
#     compressed: bool
#     size: int
#     cursor: str | None
#
#     def execute(self):
#         query = urllib.parse.urlencode({
#             "query": self.query,
#             "format": format,
#             "includeIsoform": "true",
#             # "force": "true",
#             # "sort": "score",
#             "size": "500",
#             "compressed": "true"
#         })
#         url = f"https://www.uniprot.org/{dataset}/search"
#         while True:
#             response = requests.get(url)
#             yield response
#             if link_header := response.headers.get("Link"):
#                 if url := RE_NEXT_LINK.match(link_header):
#                     continue
#             break
#
#     @root_validator
#     def fields_format(self, values: dict):
#         if format not in ["tsv", "json", "xlsx"] and len(values.get("fields", [])) > 0:
#             raise ValueError(
#                 "Fields can only be specified when the format is TSV, JSON or XLSX")
#
#     @root_validator
#     def fields_format(self, values: dict):
#         if values.get("uniprotIsoform") and values.get("dataset") != "uniprotkb":
#             raise ValueError(
#                 "Fields can only be specified when the format is TSV, JSON or XLSX")
#
#
# class ConfigurableFieldSearchKwargs(SearchKwargs):
#     """
#     Kwargs for any UniProt search, when we have specified a format that has
#     configurable fields
#     """
#     format: Literal["tsv", "json", "xlsx"]
#     fields: Iterable[str] | None
#
#
# class UnconfigurableFieldSearchKwargs(SearchKwargs):
#     """
#     Kwargs for any UniProt search, when we have specified a format that does not have
#     configurable fields
#     """
#     format: Literal["html", "txt", "xml", "rdf", "fasta", "gff", "list", "obo"]
#
#
# @overload
# def search(query: str,
#            **kwargs: Unpack[ConfigurableFieldSearchKwargs]) -> requests.Response:
#     ...
#
#
# @overload
# def search(query: str,
#            **kwargs: Unpack[UnconfigurableFieldSearchKwargs]) -> requests.Response:
#     ...
#
#
# def search(query, *, dataset="uniprotkb", format="json", fields=None, compressed=False,
#            size=500, cursor=None, **kwargs):
#     """
#     :param query: The UniProt query, as described on `the UniProt website <https://www.uniprot.org/help/text-search>`_
#     :param dataset: The UniProt database to query
#     :param format: The requested return format
#     :param fields: A list of fields to return, or None to return the default fields
#     :param compressed: Return
#     :param size:
#     :param cursor:
#     :param kwargs:
#     :return:
#     """
#     query = urllib.parse.urlencode({
#         "query": query,
#         "format": format,
#         "includeIsoform": "true",
#         # "force": "true",
#         # "sort": "score",
#         "size": "500",
#         "compressed": "true"
#     })
#     url = f"https://www.uniprot.org/{dataset}/search"
#     while True:
#         response = requests.get(url)
#         yield response
#         if link_header := response.headers.get("Link"):
#             if url := RE_NEXT_LINK.match(link_header):
#                 continue
#         break
#
#
# @overload
# def foo(a: int, b: str):
#     ...
#
#
# @overload
# def foo(a: bool):
#     ...
#
#
# def foo(*args):
#     pass
#
#
# class KbKwargs(BaseModel):
#     """
#     Shared kwargs by all UniProtKB search functions
#     """
#     includeIsoform: bool
#
#
# class ConfigurableFieldKbKwargs(SearchKwargs, KbKwargs):
#     """
#     Kwargs for searching the UniProtKB, when we have specified a format that has
#     configurable fields
#     """
#     format: Literal["tsv", "json", "xlsx"]
#     field: Iterable[str]
#
#
# class UnconfigurableFieldKbKwargs(SearchKwargs, KbKwargs):
#     """
#     Kwargs for searching the UniProtKB, when we have specified a format that does not
#     have configurable fields
#     """
#     format: Literal["html", "txt", "xml", "rdf", "fasta", "gff", "list", "obo"]
#
#
# @overload
# def search_kb(query: str | KbQuery,
#               **kwargs: Unpack[ConfigurableFieldKbKwargs]) -> requests.Response:
#     ...
#
#
# @overload
# def search_kb(query: str | KbQuery,
#               **kwargs: Unpack[UnconfigurableFieldKbKwargs]) -> requests.Response:
#     ...
#
#
# def search_kb(query, **kwargs):
#     return
