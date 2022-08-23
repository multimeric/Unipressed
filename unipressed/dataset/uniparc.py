from typing import Any, Literal, Mapping

from unipressed.dataset.core import FetchManyDataset
from unipressed.dataset.generated_types.uniparc import (
    UniparcFields,
    UniparcQuery,
    UniparcSearch,
)

UniparcFormats = Literal["fasta", "tsv", "xlsx", "json", "rdf", "xml", "list"]


class Uniparc(
    FetchManyDataset[
        UniparcQuery, Mapping[str, Any], UniparcFields, UniparcSearch, UniparcFormats
    ]
):
    @classmethod
    def name(cls):
        return "uniparc"

    @classmethod
    def bulk_endpoint(cls):
        return "upis"
