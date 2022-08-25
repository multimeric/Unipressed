from typing import Any, Literal, Mapping

from unipressed.dataset.core import FetchManyDataset
from unipressed.dataset.generated_types.uniparc import UniparcFields, UniparcQuery

UniparcFormats = Literal["fasta", "tsv", "xlsx", "json", "xml"]


class Uniparc(
    FetchManyDataset[UniparcQuery, Mapping[str, Any], UniparcFields, UniparcFormats]
):
    @classmethod
    def name(cls):
        return "uniparc"

    @classmethod
    def bulk_endpoint(cls):
        return "upis"

    @classmethod
    def id_field(cls, record: Mapping[str, Any]) -> str:
        return record["uniParcId"]
