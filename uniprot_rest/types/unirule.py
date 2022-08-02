from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest.base


class UniruleQuery(TypedDict("UniruleQuery", {})):
    and_: NotRequired[Iterable["UniruleQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["UniruleQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["UniruleQuery"]]
    "Negate a filter"
    protein_name: NotRequired[str]
    "Protein Name [DE]"
    gene: NotRequired[str]
    "Gene Name [GN]"
    organism: NotRequired[str]
    "Organism [OS]"
    taxonomy: NotRequired[str]
    "Taxonomy [OC]"
    ec: NotRequired[str]
    "Enzyme classification [EC]"
    cc_cofactor: NotRequired[str]
    cc_cofactor_note: NotRequired[str]
    cc_catalytic_activity: NotRequired[str]
    cc_activity_regulation: NotRequired[str]
    cc_pathway: NotRequired[str]
    cc_subcellular_location: NotRequired[str]
    cc_subcellular_location_note: NotRequired[str]
    cc_induction: NotRequired[str]
    cc_domain: NotRequired[str]
    family: NotRequired[str]
    "Protein family"
    cc_similarity: NotRequired[str]
    go: NotRequired[str]
    "Gene Ontology [GO]"
    keyword: NotRequired[str]
    "Keyword [KW]"


UniruleUnirule: TypeAlias = Literal[
    "rule_id",
    "template_entries",
    "statistics",
    "taxonomic_scope",
    "annotation_covered",
    "predicted_protein_name",
]
UniruleFields: TypeAlias = Literal[
    UniruleUnirule,
]


@dataclass
class UniruleSearch(uniprot_rest.base.Search):
    dataset: Literal["unirule"] = field(default="unirule", init=False)
    query: UniruleQuery
    "A query that filters the returned proteins"
    fields: Iterable[UniruleFields]
    "Fields to return in the result object"
