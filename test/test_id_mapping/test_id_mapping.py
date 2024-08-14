from time import sleep
from typing import Set

import pytest

from unipressed.id_mapping import IdMappingClient, IdMappingError


@pytest.fixture
def fifty_accessions() -> Set[str]:
    return {
        "A0A0C5B5G6",
        "A0A1B0GTW7",
        "A0JNW5",
        "A0JP26",
        "A0PK11",
        "A1A4S6",
        "A1A519",
        "A1L190",
        "A1L3X0",
        "A1X283",
        "A2A2Y4",
        "A2RU14",
        "A2RUB6",
        "A2RUC4",
        "A4D1B5",
        "A4GXA9",
        "A5D8V7",
        "A5PLL7",
        "A6BM72",
        "A6H8Y1",
        "A6NCS4",
        "A6NFY7",
        "A6NGG8",
        "A6NI61",
        "A6NKB5",
        "A6NNB3",
        "A7E2V4",
        "A7MCY6",
        "A7MD48",
        "A7XYQ1",
        "A8MQ03",
        "A8MW99",
        "A9UHW6",
        "B1AK53",
        "B1AL88",
        "B2RUY7",
        "B3KU38",
        "B6A8C7",
        "B7U540",
        "C9JLW8",
        "C9JRZ8",
        "D3W0D1",
        "E0CX11",
        "O00115",
        "O00116",
        "O00159",
        "O00161",
        "O00165",
        "O00168",
        "O00214",
    }


@pytest.fixture
def fifty_gene_names() -> Set[str]:
    return {
        "MT-RNR1",
        "CIROP",
        "BLTP3B",
        "POTEB3",
        "CLRN2",
        "ARHGAP10",
        "FAM170A",
        "SYCE3",
        "ELOVL7",
        "SH3PXD2B",
        "FRMD3",
        "TMEM218",
        "CCDC66",
        "TYW5",
        "GSAP",
        "EME2",
        "ODAD3",
        "PEDS1",
        "MEGF11",
        "BDP1",
        "NKX2-6",
        "SDHAF1",
        "PCARE",
        "MYMK",
        "PCNX2",
        "IFITM5",
        "ZSWIM8",
        "TBKBP1",
        "SRRM4",
        "SOBP",
        "CYSRT1",
        "MEI4",
        "MIF4GD",
        "ESPN",
        "NALF1",
        "VWC2L",
        "IQCJ-SCHIP1",
        "TARM1",
        "KCNJ18",
        "MCRIP1",
        "AKR1B15",
        "KLRF2",
        "STMP1",
        "DNASE2",
        "AGPS",
        "MYO1C",
        "SNAP23",
        "HAX1",
        "FXYD1",
        "LGALS8",
    }


def test_gene_names():
    inputs = {"A1L190", "A0JP26", "A0PK11"}
    outputs = {"CLRN2", "POTEB3", "SYCE3"}
    request = IdMappingClient.submit(
        source="UniProtKB_AC-ID", dest="Gene_Name", ids=inputs
    )
    # At this point it might be already finished
    assert request.get_status() in {"RUNNING", "FINISHED"}
    sleep(1)
    # At this point it should definitely be finished
    assert request.get_status() == "FINISHED"
    for result in request.each_result():
        assert result["from"] in inputs
        assert result["to"] in outputs


def test_too_slow(fifty_accessions: Set[str], fifty_gene_names: Set[str]):
    """
    If we request 50 items, but don't give uniprot enough time to process them, we should still
    handle this correctly
    """
    request = IdMappingClient.submit(
        source="UniProtKB_AC-ID", dest="Gene_Name", ids=fifty_accessions
    )
    with pytest.raises(IdMappingError):
        for result in request.each_result():
            pass


def test_paginated(fifty_accessions: Set[str], fifty_gene_names: Set[str]):
    request = IdMappingClient.submit(
        source="UniProtKB_AC-ID", dest="Gene_Name", ids=fifty_accessions
    )
    sleep(5)
    for i, result in enumerate(request.each_result()):
        assert result["from"] in fifty_accessions
        assert result["to"] in fifty_gene_names

    # We should have seen 50 entries
    assert i == 49


def test_taxon_id_yeast():
    # Checks that setting a taxon_id filter returns results from only yeast
    request = IdMappingClient.submit(
        source="Gene_Name", dest="UniProtKB", ids={"STE2"}, taxon_id=4932
    )
    sleep(5)
    results = {result["to"] for result in request.each_result()}
    assert len(results) >= 5
    # Real yeast gene
    assert "P0CI39" in results
    # Mouse gene
    assert "P14719" not in results


def test_taxon_id_all():
    # Checks that setting no taxon_id filter returns results from multiple taxa
    request = IdMappingClient.submit(source="Gene_Name", dest="UniProtKB", ids={"STE2"})
    sleep(5)
    results = {result["to"] for result in request.each_result()}
    assert len(results) > 5
    # Real yeast gene
    assert "P0CI39" in results
    # Mouse gene
    assert "P14719" in results
