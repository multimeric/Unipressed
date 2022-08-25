from typing import Any, Literal, Mapping

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.locations import LocationsFields, LocationsQuery

LocationsFormats = Literal["json", "tsv", "xlsx", "list", "obo"]


class Locations(
    UniprotDataset[
        LocationsQuery,
        Mapping[str, Any],
        LocationsFields,
        LocationsFormats,
    ]
):
    @classmethod
    def name(cls):
        return "locations"
