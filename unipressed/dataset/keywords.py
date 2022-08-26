from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import DatasetClient
from unipressed.dataset.generated_types.keywords import KeywordsFields, KeywordsQuery

KeywordsFormats = Literal["json", "tsv", "xlsx", "list", "obo"]


class KeywordsClient(
    DatasetClient[
        KeywordsQuery,
        Mapping[str, Any],
        KeywordsFields,
        KeywordsFormats,
    ]
):
    @classmethod
    def name(cls):
        return "keywords"

    @classmethod
    def _id_field(cls, record: Mapping[str, Any]) -> str:
        return record["keyword"]["id"]
