from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict


class KeywordsQueryDict(TypedDict):
    and_: NotRequired[Iterable["KeywordsQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["KeywordsQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["KeywordsQuery"]]
    "Negate a filter"
    name: NotRequired[str]
    "Name\ne.g. 2Fe-2S"
    keyword_id: NotRequired[str]
    "Keyword [AC]\ne.g. KW-0001"
    category: NotRequired[str]
    "Category\ne.g. Domain\n* technical_term: Technical term [KW-9990]\n* ptm: PTM [KW-9991]\n* molecular_function: Molecular function [KW-9992]\n* ligand: Ligand [KW-9993]\n* domain: Domain [KW-9994]\n* disease: Disease [KW-9995]\n* developmental_stage: Developmental stage [KW-9996]\n* coding_sequence_diversity: Coding sequence diversity [KW-9997]\n* cellular_component: Cellular component [KW-9998]\n* biological_process: Biological process [KW-9999]"


KeywordsQuery: TypeAlias = Union[KeywordsQueryDict, str]
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
