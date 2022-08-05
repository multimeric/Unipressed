from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class UniruleQuery(TypedDict):
    and_: NotRequired[Iterable["UniruleQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["UniruleQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["UniruleQuery"]]
    "Negate a filter"
    protein_name: NotRequired[str]
    "Protein Name [DE]\ne.g. mas5"
    gene: NotRequired[str]
    "Gene Name [GN]\ne.g. ydj1"
    organism: NotRequired[str]
    "Organism [OS]\ne.g. saccharomyces"
    taxonomy: NotRequired[str]
    "Taxonomy [OC]\ne.g. human"
    ec: NotRequired[str]
    "Enzyme classification [EC]\ne.g. 1.1.2.3"
    cc_cofactor: NotRequired[str]
    "Cc cofactor\ne.g. 29105"
    cc_cofactor_note: NotRequired[str]
    "Cc cofactor note\ne.g. subunit"
    cc_catalytic_activity: NotRequired[str]
    "Cc catalytic activity\ne.g. tyrosine"
    cc_activity_regulation: NotRequired[str]
    "Cc activity regulation\ne.g. inhibited"
    cc_pathway: NotRequired[str]
    "Cc pathway\ne.g. metabolism"
    cc_subcellular_location: NotRequired[str]
    "Cc subcellular location\ne.g. membrane"
    cc_scl_term: NotRequired[str]
    "Cc scl term"
    cc_subcellular_location_note: NotRequired[str]
    "Cc subcellular location note\ne.g. membrane"
    cc_induction: NotRequired[str]
    "Cc induction\ne.g. calcium"
    cc_domain: NotRequired[str]
    "Cc domain\ne.g. conformation"
    family: NotRequired[str]
    "Protein family\ne.g. pa28"
    cc_similarity: NotRequired[str]
    "Cc similarity\ne.g. phosphatase"
    go: NotRequired[str]
    "Gene Ontology [GO]\ne.g. 0009986"
    keyword: NotRequired[str]
    "Keyword [KW]\ne.g. chromosomal"


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
class UniruleSearch(unipressed.base.Search):
    """Client for querying the [unirule Uniprot dataset](https://www.uniprot.org/help/unirule)"""

    dataset: Literal["unirule"] = field(default="unirule", init=False)
    query: UniruleQuery
    "A query that filters the returned proteins"
    fields: Iterable[UniruleFields]
    "Fields to return in the result object"
