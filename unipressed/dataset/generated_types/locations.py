from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict


class LocationsQueryDict(TypedDict):
    and_: NotRequired[Iterable["LocationsQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["LocationsQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["LocationsQuery"]]
    "Negate a filter"
    name: NotRequired[str]
    "Name\ne.g. A band"
    id: NotRequired[str]
    "Location [AC]\ne.g. SL-0476"


LocationsQuery: TypeAlias = Union[LocationsQueryDict, str]
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
