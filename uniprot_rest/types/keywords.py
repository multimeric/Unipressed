from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest.base


class KeywordsQuery(TypedDict("KeywordsQuery", {})):
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
class KeywordsSearch(uniprot_rest.base.Search):
    dataset: Literal["keywords"] = field(default="keywords", init=False)
    query: KeywordsQuery
    "A query that filters the returned proteins"
    fields: Iterable[KeywordsFields]
    "Fields to return in the result object"
