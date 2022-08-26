from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import DatasetClient
from unipressed.dataset.generated_types.unirule import UniruleFields, UniruleQuery

UniruleFormats = Literal["json", "list"]


class UniruleClient(
    DatasetClient[UniruleQuery, Mapping[str, Any], UniruleFields, UniruleFormats]
):
    @classmethod
    def name(cls):
        return "unirule"

    @classmethod
    def _id_field(cls, record: Mapping[str, Any]) -> str:
        return record["uniRuleId"]
