from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import DatasetClient
from unipressed.dataset.generated_types.locations import LocationsFields, LocationsQuery

LocationsFormats = Literal["json", "tsv", "xlsx", "list", "obo"]


class LocationsClient(
    DatasetClient[
        LocationsQuery,
        Mapping[str, Any],
        LocationsFields,
        LocationsFormats,
    ]
):
    @classmethod
    def name(cls):
        return "locations"
