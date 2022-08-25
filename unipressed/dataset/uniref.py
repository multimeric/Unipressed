from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import FetchManyDataset
from unipressed.dataset.generated_types.uniref import UnirefFields, UnirefQuery

UnirefFormats = Literal["fasta", "tsv", "json", "xlsx", "list"]


class Uniref(
    FetchManyDataset[UnirefQuery, Mapping[str, Any], UnirefFields, UnirefFormats]
):
    @classmethod
    def name(cls):
        return "uniref"

    @classmethod
    def bulk_endpoint(cls):
        return "ids"
