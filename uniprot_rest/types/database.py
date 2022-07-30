from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

DatabaseQuery: TypeAlias = TypedDict(
    "DatabaseQuery", {"name": NotRequired[str], "id": NotRequired[str]}
)
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
class DatabaseSearch(uniprot_rest.Search):
    dataset: Literal["database"] = field(default="database", init=False)
    query: DatabaseQuery
    fields: DatabaseFields
