from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import FetchManyClient
from unipressed.dataset.generated_types.taxonomy import TaxonomyFields, TaxonomyQuery

TaxonomyFormats = Literal["json", "tsv", "xlsx", "list"]


class TaxonomyClient(
    FetchManyClient[
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
    def _bulk_endpoint(cls):
        return "taxonIds"

    @classmethod
    def _id_field(cls, record: Mapping[str, Any]) -> str:
        return record["taxonId"]
