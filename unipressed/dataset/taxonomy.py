from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import FetchManyDataset
from unipressed.dataset.generated_types.taxonomy import TaxonomyFields, TaxonomyQuery

TaxonomyFormats = Literal["json", "tsv", "xlsx", "list"]


class Taxonomy(
    FetchManyDataset[
        TaxonomyQuery,
        Mapping[str, Any],
        TaxonomyFields,
        TaxonomyFormats,
    ]
):
    @classmethod
    def name(cls):
        return "taxonomy"

    @classmethod
    def bulk_endpoint(cls):
        return "taxonIds"

    @classmethod
    def id_field(cls, record: Mapping[str, Any]) -> str:
        return record["taxonId"]
