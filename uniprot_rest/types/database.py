from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest.base


class DatabaseQuery(TypedDict("DatabaseQuery", {})):
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
class DatabaseSearch(uniprot_rest.base.Search):
    dataset: Literal["database"] = field(default="database", init=False)
    query: DatabaseQuery
    "A query that filters the returned proteins"
    fields: Iterable[DatabaseFields]
    "Fields to return in the result object"
