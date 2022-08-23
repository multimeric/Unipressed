from typing import Any, Literal, Mapping

from unipressed.dataset.core import FetchManyDataset
from unipressed.dataset.generated_types.uniref import (
    UnirefFields,
    UnirefQuery,
    UnirefSearch,
)

UnirefFormats = Literal["fasta", "tsv", "json", "xlsx", "list"]


class Uniref(
    FetchManyDataset[
        UnirefQuery, Mapping[str, Any], UnirefFields, UnirefSearch, UnirefFormats
    ]
):
    @classmethod
    def name(cls):
        return "uniref"

    @classmethod
    def bulk_endpoint(cls):
        return "ids"
