from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class LocationsQuery(TypedDict):
    and_: NotRequired[Iterable["LocationsQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["LocationsQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["LocationsQuery"]]
    "Negate a filter"
    name: NotRequired[str]
    "Name"
    id: NotRequired[str]
    "Location [AC]"


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
class LocationsSearch(unipressed.base.Search):
    """Client for querying the [locations Uniprot dataset](https://www.uniprot.org/help/locations)"""

    dataset: Literal["locations"] = field(default="locations", init=False)
    query: LocationsQuery
    "A query that filters the returned proteins"
    fields: Iterable[LocationsFields]
    "Fields to return in the result object"
