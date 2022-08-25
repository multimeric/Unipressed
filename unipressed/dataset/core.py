from __future__ import annotations

import gzip
from abc import ABCMeta, abstractmethod
from io import IOBase
from typing import Generic, Iterable, Type, overload

import requests
from typing_extensions import Literal, get_args

from unipressed.dataset.search import Search
from unipressed.dataset.type_vars import (
    FieldsType,
    FormatType,
    JsonResultType,
    QueryType,
)


class UniprotDataset(
    Generic[QueryType, JsonResultType, FieldsType, FormatType],
    metaclass=ABCMeta,
):
    @classmethod
    def id_field(cls, record: JsonResultType) -> str:
        """
        Given a record, extracts the accession/ID field from it
        """
        return record["id"]

    @classmethod
    @abstractmethod
    def name(cls) -> str:
        ...

    @classmethod
    def search(
        cls,
        query: QueryType,
        format: FormatType | Literal["json"] = "json",
        fields: Iterable[FieldsType] | None = None,
        size: int = 500,
    ) -> Search[QueryType, JsonResultType, FieldsType, FormatType]:
        """
        Creates an object that can be used to perform a search query over this dataset
        """
        return Search[QueryType, JsonResultType, FieldsType, FormatType](
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
        """
        Fetches a single record from this dataset from its ID

        Args:
            id : The ID of the record to fetch. The format of this will depend on the dataset
            format : The format of the result
            parse : If true, parse the result into a JSON dictionary. Defaults to True.
        """
        res = requests.get(
            f"https://rest.uniprot.org/{cls.name()}/{id}.{format}", stream=True
        )
        res.raise_for_status()
        if parse and format == "json":
            return res.json()
        elif res.headers.get("Content-Encoding", None) == "gzip":
            return gzip.open(res.raw, "rb")
        else:
            return res.raw

    @classmethod
    def _type_args(cls) -> tuple[Type, ...]:
        """
        Returns the type arguments for this dataset
        """
        return get_args(cls.__orig_bases__[0])  # type: ignore

    @classmethod
    def _allowed_query_fields(cls) -> set[str]:
        """
        Returns the type arguments for the queries to this dataset
        """
        query_dict, _ = get_args(cls._query_type())
        return query_dict.__optional_keys__ | query_dict.__required_keys__ - {
            "and_",
            "or_",
            "not_",
        }

    @classmethod
    def _allowed_return_fields(cls) -> set[str]:
        """
        Returns the type arguments for the queries to this dataset
        """
        return set(get_args(cls._field_type()))

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
    def _format_type(cls):
        """
        Returns the type of allowed formats for search queries
        """
        return cls._type_args()[3]

    @classmethod
    def _allowed_formats(cls) -> set[str]:
        """
        Returns a set of allowed formats
        """
        return set(get_args(cls._format_type()))


class FetchManyDataset(
    UniprotDataset[QueryType, JsonResultType, FieldsType, FormatType]
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
        elif res.headers.get("Content-Encoding", None) == "gzip":
            return gzip.open(res.raw, "rb")
        else:
            return res.raw