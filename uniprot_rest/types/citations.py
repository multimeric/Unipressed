from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

CitationsQuery: TypeAlias = TypedDict(
    "CitationsQuery",
    {
        "title": NotRequired[str],
        "author": NotRequired[str],
        "journal": NotRequired[str],
        "published": NotRequired[str],
        "id": NotRequired[str],
        "doi": NotRequired[str],
    },
)
CitationsLiterature: TypeAlias = Literal[
    "id",
    "doi",
    "title",
    "authors",
    "authoring_group",
    "journal",
    "publication_date",
    "first_page",
    "last_page",
    "volume",
    "reference",
    "lit_abstract",
    "statistics",
]
CitationsFields: TypeAlias = Literal[
    CitationsLiterature,
]


@dataclass
class CitationsSearch(uniprot_rest.Search):
    dataset: Literal["citations"] = field(default="citations", init=False)
    query: CitationsQuery
    fields: CitationsFields
