from typing import Any, Literal, Mapping

from unipressed.dataset.core import FetchManyDataset
from unipressed.dataset.generated_types.taxonomy import (
    TaxonomyFields,
    TaxonomyQuery,
    TaxonomySearch,
)

TaxonomyFormats = Literal["json", "tsv", "xlsx", "list"]


class Taxonomy(
    FetchManyDataset[
        TaxonomyQuery,
        Mapping[str, Any],
        TaxonomyFields,
        TaxonomySearch,
        TaxonomyFormats,
    ]
):
    @classmethod
    def name(cls):
        return "taxonomy"

    @classmethod
    def bulk_endpoint(cls):
        return "taxonIds"
