from typing import Any, Literal, Mapping

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.keywords import (
    KeywordsFields,
    KeywordsQuery,
    KeywordsSearch,
)

KeywordsFormats = Literal["json", "tsv", "xlsx", "list", "obo"]


class Keywords(
    UniprotDataset[
        KeywordsQuery,
        Mapping[str, Any],
        KeywordsFields,
        KeywordsSearch,
        KeywordsFormats,
    ]
):
    @classmethod
    def name(cls):
        return "keywords"

    @classmethod
    def id_field(cls, record: Mapping[str, Any]) -> str:
        return record["keyword"]["id"]
