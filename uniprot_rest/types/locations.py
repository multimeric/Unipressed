from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

LocationsQuery: TypeAlias = TypedDict(
    "LocationsQuery", {"name": NotRequired[str], "id": NotRequired[str]}
)
LocationsSubcellularLocation: TypeAlias = Literal[
    "id",
    "name",
    "definition",
    "category",
    "keyword",
    "synonyms",
    "content",
    "gene_ontologies",
    "note",
    "references",
    "links",
    "is_a",
    "part_of",
    "statistics",
]
LocationsFields: TypeAlias = Literal[
    LocationsSubcellularLocation,
]


@dataclass
class LocationsSearch(uniprot_rest.Search):
    dataset: Literal["locations"] = field(default="locations", init=False)
    query: LocationsQuery
    fields: LocationsFields
