from typing import Any, Literal, Mapping

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.arba import ArbaFields, ArbaQuery, ArbaSearch

ArbaFormats = Literal["json", "list"]


class Arba(
    UniprotDataset[ArbaQuery, Mapping[str, Any], ArbaFields, ArbaSearch, ArbaFormats]
    @ classmethod
):
    def name(cls):
        return "arba"

    @classmethod
    def id_field(cls) -> str:
        return "uniRuleId"
