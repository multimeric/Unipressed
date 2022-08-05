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
    "Name\ne.g. 2Fe-2S"
    keyword_id: NotRequired[str]
    "Keyword [AC]\ne.g. KW-0001"
    category: NotRequired[str]
    "Category\n\ntechnical_term: Technical term [KW-9990]\n\nptm: PTM [KW-9991]\n\nmolecular_function: Molecular function [KW-9992]\n\nligand: Ligand [KW-9993]\n\ndomain: Domain [KW-9994]\n\ndisease: Disease [KW-9995]\n\ndevelopmental_stage: Developmental stage [KW-9996]\n\ncoding_sequence_diversity: Coding sequence diversity [KW-9997]\n\ncellular_component: Cellular component [KW-9998]\n\nbiological_process: Biological process [KW-9999]\ne.g. Domain"


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
