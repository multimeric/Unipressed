from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import DatasetClient
from unipressed.dataset.generated_types.database import DatabaseFields, DatabaseQuery

DatabaseFormats = Literal["json"]


class DatabaseClient(
    DatasetClient[
        DatabaseQuery,
        Mapping[str, Any],
        DatabaseFields,
        DatabaseFormats,
    ]
):
    @classmethod
    def name(cls):
        return "database"
