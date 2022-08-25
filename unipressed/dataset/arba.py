from typing import Any, Literal, Mapping

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.arba import ArbaFields, ArbaQuery

ArbaFormats = Literal["json", "list"]


class Arba(UniprotDataset[ArbaQuery, Mapping[str, Any], ArbaFields, ArbaFormats]):
    @classmethod
    def name(cls):
        return "arba"

    @classmethod
    def id_field(cls, record: Any) -> str:
        return record["uniRuleId"]
