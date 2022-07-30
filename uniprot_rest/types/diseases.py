from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

DiseasesQuery: TypeAlias = TypedDict(
    "DiseasesQuery", {"name": NotRequired[str], "id": NotRequired[str]}
)
DiseasesDisease: TypeAlias = Literal[
    "id",
    "name",
    "acronym",
    "definition",
    "alternative_names",
    "cross_references",
    "keywords",
    "statistics",
]
DiseasesFields: TypeAlias = Literal[
    DiseasesDisease,
]


@dataclass
class DiseasesSearch(uniprot_rest.Search):
    dataset: Literal["diseases"] = field(default="diseases", init=False)
    query: DiseasesQuery
    fields: DiseasesFields
