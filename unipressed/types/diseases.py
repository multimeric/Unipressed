from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class DiseasesQuery(TypedDict):
    and_: NotRequired[Iterable["DiseasesQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["DiseasesQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["DiseasesQuery"]]
    "Negate a filter"
    name: NotRequired[str]
    "Name"
    id: NotRequired[str]
    "Disease [AC]"


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
class DiseasesSearch(unipressed.base.Search):
    """Client for querying the [diseases Uniprot dataset](https://www.uniprot.org/help/diseases)"""

    dataset: Literal["diseases"] = field(default="diseases", init=False)
    query: DiseasesQuery
    "A query that filters the returned proteins"
    fields: Iterable[DiseasesFields]
    "Fields to return in the result object"
