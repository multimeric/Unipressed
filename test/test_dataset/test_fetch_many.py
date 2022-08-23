import codecs

import skbio

from unipressed import Uniprotkb


def test_uniprotkb_json():
    ids = ["A0A0C5B5G6", "A0A1B0GTW7"]
    for record in Uniprotkb.fetch_many():
        assert isinstance(record, dict)
        assert record["primaryAccession"] in ids


def test_uniprotkb_fasta():
    ids = ["A0A0C5B5G6", "A0A1B0GTW7"]
    res = Uniprotkb.fetch_many(["A0A0C5B5G6", "A0A1B0GTW7"], format="fasta")
    text_stream = codecs.getreader("utf-8")(res)
    for record in skbio.io.read(text_stream, format="fasta"):
        assert any([id in record.metadata["id"] for id in ids])
