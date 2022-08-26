from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import FetchManyClient
from unipressed.dataset.generated_types.uniparc import UniparcFields, UniparcQuery

UniparcFormats = Literal["fasta", "tsv", "xlsx", "json", "xml"]


class UniparcClient(
    FetchManyClient[UniparcQuery, Mapping[str, Any], UniparcFields, UniparcFormats]
):
    @classmethod
    def name(cls):
        return "uniparc"

    @classmethod
    def _bulk_endpoint(cls):
        return "upis"

    @classmethod
    def _id_field(cls, record: Mapping[str, Any]) -> str:
        return record["uniParcId"]
