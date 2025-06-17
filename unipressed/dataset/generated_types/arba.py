from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict


class ArbaQueryDict(TypedDict):
    and_: NotRequired[Iterable["ArbaQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["ArbaQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["ArbaQuery"]]
    "Negate a filter"
    protein_name: NotRequired[str]
    "Protein Name [DE]\ne.g. Elastin"
    taxonomy: NotRequired[str]
    "Taxonomy [OC]\ne.g. human"
    ec: NotRequired[str]
    "Enzyme classification [EC]\ne.g. 2.3.2.5"
    cc_cofactor: NotRequired[str]
    "Cofactor\ne.g. 29105"
    cc_catalytic_activity: NotRequired[str]
    "Catalytic activity\ne.g. tyrosine"
    cc_pathway: NotRequired[str]
    "Pathway\ne.g. metabolism"
    cc_subcellular_location: NotRequired[str]
    "Subcellular location [CC]\ne.g. membrane"
    family: NotRequired[str]
    "Protein family\ne.g. pa28"
    cc_similarity: NotRequired[str]
    "Comment similarity\ne.g. phosphatase"
    keyword: NotRequired[str]
    "Keyword [KW]\ne.g. Tight junction"


ArbaQuery: TypeAlias = Union[ArbaQueryDict, str]
ArbaArba: TypeAlias = Literal[
    "rule_id", "statistics", "taxonomic_scope", "annotation_covered"
]
ArbaFields: TypeAlias = Literal[ArbaArba,]
