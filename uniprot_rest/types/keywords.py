from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

KeywordsQuery: TypeAlias = TypedDict(
    "KeywordsQuery",
    {
        "name": NotRequired[str],
        "keyword_id": NotRequired[str],
        "category": NotRequired[str],
    },
)
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
class KeywordsSearch(uniprot_rest.Search):
    dataset: Literal["keywords"] = field(default="keywords", init=False)
    query: KeywordsQuery
    fields: KeywordsFields
