from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import DatasetClient
from unipressed.dataset.generated_types.citations import CitationsFields, CitationsQuery

CitationsFormats = Literal["json", "list", "tsv", "xlsx"]


class CitationsClient(
    DatasetClient[
        CitationsQuery,
        Mapping[str, Any],
        CitationsFields,
        CitationsFormats,
    ]
):
    @classmethod
    def name(cls):
        return "citations"

    @classmethod
    def _id_field(cls, record: Any) -> str:
        return record["citation"]["id"]
