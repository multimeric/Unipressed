from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.database import DatabaseFields, DatabaseQuery

DatabaseFormats = Literal["json"]


class Database(
    UniprotDataset[
        DatabaseQuery,
        Mapping[str, Any],
        DatabaseFields,
        DatabaseFormats,
    ]
):
    @classmethod
    def name(cls):
        return "database"
