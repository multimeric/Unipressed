from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class CitationsQuery(TypedDict):
    and_: NotRequired[Iterable["CitationsQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["CitationsQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["CitationsQuery"]]
    "Negate a filter"
    title: NotRequired[str]
    "Title"
    author: NotRequired[str]
    "Author"
    journal: NotRequired[str]
    "Journal"
    published: NotRequired[str]
    "Year published"
    id: NotRequired[str]
    "Citation Id"
    doi: NotRequired[str]
    "DOI"


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
class CitationsSearch(unipressed.base.Search):
    """Client for querying the [citations Uniprot dataset](https://www.uniprot.org/help/citations)"""

    dataset: Literal["citations"] = field(default="citations", init=False)
    query: CitationsQuery
    "A query that filters the returned proteins"
    fields: Iterable[CitationsFields]
    "Fields to return in the result object"
