import codecs
import sys

import pytest

from unipressed import UniprotkbClient


def test_uniprotkb_json():
    ids = ["A0A0C5B5G6", "A0A1B0GTW7"]
    for record in UniprotkbClient.fetch_many(ids):
        assert isinstance(record, dict)
        assert record["primaryAccession"] in ids


def test_uniprotkb_fasta():
    import fastaparser

    ids = ["A0A0C5B5G6", "A0A1B0GTW7"]
    res = UniprotkbClient.fetch_many(["A0A0C5B5G6", "A0A1B0GTW7"], format="fasta")
    text_stream = codecs.getreader("utf-8")(res)
    for record in fastaparser.Reader(text_stream):
        assert any([id in record.id for id in ids])
