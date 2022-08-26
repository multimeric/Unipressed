from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict


class DatabaseQueryDict(TypedDict):
    and_: NotRequired[Iterable["DatabaseQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["DatabaseQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["DatabaseQuery"]]
    "Negate a filter"
    name: NotRequired[str]
    "Name\ne.g. Arabidopsis Information Portal"
    id: NotRequired[str]
    "Database [AC]\ne.g. DB-0236"


DatabaseQuery: TypeAlias = Union[DatabaseQueryDict, str]
DatabaseCrossReference: TypeAlias = Literal[
    "id",
    "name",
    "abbrev",
    "pubmed_id",
    "doi_id",
    "link_type",
    "server",
    "dbUrl",
    "category",
    "statistics",
]
DatabaseFields: TypeAlias = Literal[
    DatabaseCrossReference,
]
