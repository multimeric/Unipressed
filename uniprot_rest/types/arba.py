from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

ArbaQuery: TypeAlias = TypedDict(
    "ArbaQuery",
    {
        "protein_name_field": NotRequired[str],
        "organism_field": NotRequired[str],
        "taxonomy_field": NotRequired[str],
        "ec": NotRequired[str],
        "cc_cofactor": NotRequired[str],
        "cc_catalytic_activity_field": NotRequired[str],
        "cc_activity_regulation": NotRequired[str],
        "cc_pathway": NotRequired[str],
        "cc_scl_term_field": NotRequired[str],
        "cc_scl_note": NotRequired[str],
        "cc_domain": NotRequired[str],
        "family": NotRequired[str],
        "cc_similarity": NotRequired[str],
        "keyword_field": NotRequired[str],
    },
)
ArbaArba: TypeAlias = Literal[
    "rule_id", "statistics", "taxonomic_scope", "annotation_covered"
]
ArbaFields: TypeAlias = Literal[
    ArbaArba,
]


@dataclass
class ArbaSearch(uniprot_rest.Search):
    dataset: Literal["arba"] = field(default="arba", init=False)
    query: ArbaQuery
    fields: ArbaFields
