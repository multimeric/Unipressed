from unipressed import Uniprotkb


def test_uniprotkb_parsed():
    ret = Uniprotkb.fetch_one("A1A519")

    assert isinstance(ret, dict)
    assert ret["primaryAccession"] == "A1A519"
    assert ret["uniProtkbId"] == "F170A_HUMAN"


def test_uniprotkb_fasta():
    import io

    ret = Uniprotkb.fetch_one("A1A519", format="fasta")

    assert isinstance(ret, io.IOBase)
    content = ret.read()
    assert content.startswith(b">sp|A1A519|F170A_HUMAN")
    assert b"KLIHSGIQRIHRDSPQ" in content
