import codecs
import sys

import pytest

from unipressed import UniprotkbClient


def test_uniprotkb_json():
    ids = ["A0A0C5B5G6", "A0A1B0GTW7"]
    for record in UniprotkbClient.fetch_many(ids):
        assert isinstance(record, dict)
        assert record["primaryAccession"] in ids


@pytest.mark.skipif(
    sys.version_info < (3, 8) or sys.version_info > (3, 10),
    reason="skbio is fussy about the Python versions it supports",
)
def test_uniprotkb_fasta():
    import skbio

    ids = ["A0A0C5B5G6", "A0A1B0GTW7"]
    res = UniprotkbClient.fetch_many(["A0A0C5B5G6", "A0A1B0GTW7"], format="fasta")
    text_stream = codecs.getreader("utf-8")(res)
    for record in skbio.io.read(text_stream, format="fasta"):
        assert any([id in record.metadata["id"] for id in ids])
