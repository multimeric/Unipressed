from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from datetime import date


class DiseasesQueryDict(TypedDict):
    and_: NotRequired[Iterable["DiseasesQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["DiseasesQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["DiseasesQuery"]]
    "Negate a filter"
    name: NotRequired[str]
    "Name\ne.g. alzheimer disease"
    id: NotRequired[str]
    "Disease [AC]\ne.g. DI-12345"


DiseasesQuery: TypeAlias = Union[DiseasesQueryDict, str]
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
