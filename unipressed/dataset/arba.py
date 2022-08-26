from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.arba import ArbaFields, ArbaQuery

ArbaFormats = Literal["json", "list"]


class Arba(UniprotDataset[ArbaQuery, Mapping[str, Any], ArbaFields, ArbaFormats]):
    @classmethod
    def name(cls):
        return "arba"

    @classmethod
    def _id_field(cls, record: Any) -> str:
        return record["uniRuleId"]
