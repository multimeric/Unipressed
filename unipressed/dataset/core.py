from __future__ import annotations

import gzip
from abc import ABC, ABCMeta, abstractmethod
from ast import Bytes
from io import IOBase
from typing import (
    Any,
    Generic,
    Iterable,
    Literal,
    Mapping,
    Type,
    TypedDict,
    TypeVar,
    Union,
    get_args,
    overload,
)

import requests
from typing_extensions import TypeAlias

from unipressed.dataset.search import Search

QueryType = TypeVar("QueryType")
JsonResultType = TypeVar("JsonResultType", bound=Mapping[str, Any])
FieldsType = TypeVar("FieldsType", bound=Iterable[str])
SearchType = TypeVar("SearchType", bound=Search)
FormatType = TypeVar("FormatType", bound=str)


class UniprotDataset(
    Generic[QueryType, JsonResultType, FieldsType, SearchType, FormatType],
    metaclass=ABCMeta,
):
    @classmethod
    def id_field(cls) -> str:
        return "primaryAccession"

    @staticmethod
    @abstractmethod
    def name() -> str:
        ...

    @classmethod
    def search(
        cls,
        query: QueryType,
        format: FormatType | Literal["json"] = "json",
        fields: Iterable[FieldsType] | None = None,
        size: int = 500,
    ) -> Search:
        return Search(
            query=query, format=format, dataset=cls.name(), fields=fields, size=size
        )

    @overload
    @classmethod
    def fetch_one(
        cls, id: str, format: Literal["json"] = "json", parse: Literal[True] = True
    ) -> JsonResultType:
        ...

    @overload
    @classmethod
    def fetch_one(
        cls, id: str, format: FormatType, parse: Literal[False] = False
    ) -> IOBase:
        ...

    @classmethod
    def fetch_one(cls, id, format="json", parse=True):
        res = requests.get(
            f"https://rest.uniprot.org/{cls.name()}/{id}.{format}", stream=True
        )
        res.raise_for_status()
        if parse and format == "json":
            return res.json()
        else:
            return res.raw

    @classmethod
    def _type_args(cls) -> tuple[Type, ...]:
        """
        Returns the type arguments for this dataset
        """
        return get_args(cls.__orig_bases__[0])

    @classmethod
    def _query_type(cls):
        """
        Returns the type arguments for the queries to this dataset
        """
        return cls._type_args()[0]

    @classmethod
    def _result_type(cls):
        """
        Returns the type of query results to this dataset
        """
        return cls._type_args()[1]

    @classmethod
    def _field_type(cls):
        """
        Returns the type of allowed fields for search queries
        """
        return cls._type_args()[2]

    @classmethod
    def _search_type(cls):
        """
        Returns the type of the Search subclass for this dataset
        """
        return cls._type_args()[3]

    @classmethod
    def _format_type(cls):
        """
        Returns the type of allowed formats for search queries
        """
        return cls._type_args()[4]

    @classmethod
    def _allowed_formats(cls) -> set[str]:
        """
        Returns a set of allowed formats
        """
        return set(get_args(cls._format_type()))


class FetchManyDataset(
    UniprotDataset[QueryType, JsonResultType, FieldsType, SearchType, FormatType]
):
    """
    Subset of datasets that can be queried by multiple IDs
    """

    @classmethod
    @abstractmethod
    def bulk_id_param(cls) -> str:
        """
        The name of the GET query parameter used to define the list of IDs in a bulk query
        """
        return cls.bulk_endpoint()

    @classmethod
    @abstractmethod
    def bulk_endpoint(cls) -> str:
        """
        The name of the URL used to query a bulk list of IDs
        """
        ...

    @overload
    @classmethod
    def fetch_many(
        cls,
        ids: Iterable[str],
        format: Literal["json"] = "json",
        parse: Literal[True] = True,
    ) -> Iterable[JsonResultType]:
        ...

    @overload
    @classmethod
    def fetch_many(
        cls, ids: Iterable[str], format: FormatType, parse: Literal[False] = False
    ) -> IOBase:
        ...

    @classmethod
    def fetch_many(
        cls,
        ids: Iterable[str],
        format: FormatType | Literal["json"] = "json",
        parse: bool = True,
    ):
        """
        Fetches multiple records using their accessions.

        Args:
            ids : The accessions to query
            format : The format to return the records. Defaults to "json".
            parse : Only supported for JSON. If True, parses the result instead of returning a raw file. Defaults to True.

        Returns:
            : If parse is True, a list of dictionaries. Otherwise, a file object containing the results in the specified format.
        """
        res = requests.get(
            f"https://rest.uniprot.org/{cls.name()}/{cls.bulk_endpoint()}",
            params={cls.bulk_id_param(): ",".join(ids), "format": format},
            stream=True,
        )
        res.raise_for_status()
        if parse and format == "json":
            return res.json()["results"]
        else:
            return gzip.open(res.raw, "rb")
