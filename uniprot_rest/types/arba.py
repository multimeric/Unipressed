from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest.base


class ArbaQuery(TypedDict("ArbaQuery", {})):
    and_: NotRequired[Iterable["ArbaQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["ArbaQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["ArbaQuery"]]
    "Negate a filter"
    protein_name: NotRequired[str]
    "Protein Name [DE]"
    organism: NotRequired[str]
    "Organism [OS]"
    taxonomy: NotRequired[str]
    "Taxonomy [OC]"
    ec: NotRequired[str]
    "Enzyme classification [EC]"
    cc_cofactor: NotRequired[str]
    cc_catalytic_activity: NotRequired[str]
    cc_activity_regulation: NotRequired[str]
    cc_pathway: NotRequired[str]
    cc_subcellular_location: NotRequired[str]
    cc_subcellular_location_note: NotRequired[str]
    cc_domain: NotRequired[str]
    family: NotRequired[str]
    "Protein family"
    cc_similarity: NotRequired[str]
    keyword: NotRequired[str]
    "Keyword [KW]"


ArbaArba: TypeAlias = Literal[
    "rule_id", "statistics", "taxonomic_scope", "annotation_covered"
]
ArbaFields: TypeAlias = Literal[
    ArbaArba,
]


@dataclass
class ArbaSearch(uniprot_rest.base.Search):
    dataset: Literal["arba"] = field(default="arba", init=False)
    query: ArbaQuery
    "A query that filters the returned proteins"
    fields: Iterable[ArbaFields]
    "Fields to return in the result object"
