from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

UniruleQuery: TypeAlias = TypedDict(
    "UniruleQuery",
    {
        "protein_name_field": NotRequired[str],
        "gene_name_field": NotRequired[str],
        "organism_field": NotRequired[str],
        "taxonomy_field": NotRequired[str],
        "ec": NotRequired[str],
        "cc_cofactor": NotRequired[str],
        "cc_cofactor_note": NotRequired[str],
        "cc_catalytic_activity_field": NotRequired[str],
        "cc_activity_regulation": NotRequired[str],
        "cc_pathway": NotRequired[str],
        "cc_scl_term_field": NotRequired[str],
        "cc_scl_note": NotRequired[str],
        "cc_induction": NotRequired[str],
        "cc_domain": NotRequired[str],
        "family": NotRequired[str],
        "cc_similarity": NotRequired[str],
        "go_field": NotRequired[str],
        "keyword_field": NotRequired[str],
    },
)
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
class UniruleSearch(uniprot_rest.Search):
    dataset: Literal["unirule"] = field(default="unirule", init=False)
    query: UniruleQuery
    fields: UniruleFields
