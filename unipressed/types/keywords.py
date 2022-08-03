from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class KeywordsQuery(TypedDict):
    and_: NotRequired[Iterable["KeywordsQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["KeywordsQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["KeywordsQuery"]]
    "Negate a filter"
    name: NotRequired[str]
    "Name"
    keyword_id: NotRequired[str]
    "Keyword [AC]"
    category: NotRequired[str]
    "Category"


KeywordsKeyword: TypeAlias = Literal[
    "id",
    "name",
    "definition",
    "category",
    "synonyms",
    "gene_ontologies",
    "links",
    "children",
    "parents",
    "statistics",
]
KeywordsFields: TypeAlias = Literal[
    KeywordsKeyword,
]


@dataclass
class KeywordsSearch(unipressed.base.Search):
    """Client for querying the [keywords Uniprot dataset](https://www.uniprot.org/help/keywords)"""

    dataset: Literal["keywords"] = field(default="keywords", init=False)
    query: KeywordsQuery
    "A query that filters the returned proteins"
    fields: Iterable[KeywordsFields]
    "Fields to return in the result object"
