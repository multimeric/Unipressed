from typing import Any, Literal, Mapping

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.unirule import (
    UniruleFields,
    UniruleQuery,
    UniruleSearch,
)

UniruleFormats = Literal["json", "list"]


class Unirule(
    UniprotDataset[
        UniruleQuery, Mapping[str, Any], UniruleFields, UniruleSearch, UniruleFormats
    ]
):
    @classmethod
    def name(cls):
        return "unirule"

    @classmethod
    def id_field(cls, record: Mapping[str, Any]) -> str:
        return record["uniRuleId"]
