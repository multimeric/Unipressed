from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import FetchManyClient
from unipressed.dataset.generated_types.uniprotkb import UniprotkbFields, UniprotkbQuery

UniprotkbFormats = Literal["txt", "xml", "fasta", "gff", "json", "list", "tsv", "xlsx"]


class UniprotkbClient(
    FetchManyClient[
        UniprotkbQuery,
        Mapping[str, Any],
        UniprotkbFields,
        UniprotkbFormats,
    ]
):
    @classmethod
    def name(cls):
        return "uniprotkb"

    @classmethod
    def _bulk_endpoint(cls):
        return "accessions"

    @classmethod
    def _id_field(cls, record: Mapping[str, Any]) -> str:
        return record["primaryAccession"]
