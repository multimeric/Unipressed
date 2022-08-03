from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class ArbaQuery(TypedDict):
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
class ArbaSearch(unipressed.base.Search):
    """Client for querying the [arba Uniprot dataset](https://www.uniprot.org/help/arba)"""

    dataset: Literal["arba"] = field(default="arba", init=False)
    query: ArbaQuery
    "A query that filters the returned proteins"
    fields: Iterable[ArbaFields]
    "Fields to return in the result object"
