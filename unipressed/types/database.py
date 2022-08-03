from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class DatabaseQuery(TypedDict):
    and_: NotRequired[Iterable["DatabaseQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["DatabaseQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["DatabaseQuery"]]
    "Negate a filter"
    name: NotRequired[str]
    "Name"
    id: NotRequired[str]
    "Database [AC]"


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


@dataclass
class DatabaseSearch(unipressed.base.Search):
    """Client for querying the [database Uniprot dataset](https://www.uniprot.org/help/database)"""

    dataset: Literal["database"] = field(default="database", init=False)
    query: DatabaseQuery
    "A query that filters the returned proteins"
    fields: Iterable[DatabaseFields]
    "Fields to return in the result object"
