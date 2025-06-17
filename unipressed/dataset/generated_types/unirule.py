from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict


class UniruleQueryDict(TypedDict):
    and_: NotRequired[Iterable["UniruleQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["UniruleQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["UniruleQuery"]]
    "Negate a filter"
    protein_name: NotRequired[str]
    "Protein Name [DE]\ne.g. Malate dehydrogenase"
    gene: NotRequired[str]
    "Gene Name [GN]\ne.g. rbfA"
    organism: NotRequired[str]
    "Organism [OS]\ne.g. Helicobacter pylori"
    taxonomy: NotRequired[str]
    "Taxonomy [OC]\ne.g. Fungi"
    ec: NotRequired[str]
    "Enzyme classification [EC]\ne.g. 4.1.1.39"
    cc_cofactor: NotRequired[str]
    "Cofactor\ne.g. 29105"
    cc_cofactor_note: NotRequired[str]
    "Cofactor note\ne.g. subunit"
    cc_catalytic_activity: NotRequired[str]
    "Catalytic activity\ne.g. tyrosine"
    cc_activity_regulation: NotRequired[str]
    "Activity regulation\ne.g. inhibited"
    cc_pathway: NotRequired[str]
    "Pathway\ne.g. metabolism"
    cc_subcellular_location: NotRequired[str]
    "Subcellular location term\ne.g. membrane"
    cc_subcellular_location_note: NotRequired[str]
    "Note\ne.g. membrane"
    cc_induction: NotRequired[str]
    "Induction\ne.g. maltose"
    cc_domain: NotRequired[str]
    "Domain comments [CC]\ne.g. DNA-binding domain"
    family: NotRequired[str]
    "Protein family\ne.g. Tyr protein kinase family"
    cc_similarity: NotRequired[str]
    "Comment similarity\ne.g. MPI phosphatase"
    go: NotRequired[str]
    "Gene Ontology [GO]\ne.g. 0009986"
    keyword: NotRequired[str]
    "Keyword [KW]\ne.g. Activator"


UniruleQuery: TypeAlias = Union[UniruleQueryDict, str]
UniruleUnirule: TypeAlias = Literal[
    "rule_id",
    "template_entries",
    "statistics",
    "taxonomic_scope",
    "annotation_covered",
    "predicted_protein_name",
]
UniruleFields: TypeAlias = Literal[UniruleUnirule,]
