from datetime import date
from typing import Iterable

from unipressed import *
from unipressed.base import Search


def make_request(**kwargs) -> Search:
    defaults = dict(
        query="taxonomy_id:9606 AND length:[2500 TO *]",
        dataset="uniprotkb",
        format="json",
        fields=["length"],
    )
    defaults.update(kwargs)
    return Search(**defaults)  # type: ignore


def test_search_pages():
    import json

    i = 0

    for i, page in enumerate(make_request().each_page()):
        # Test that it's valid JSON
        json.load(page)

    # Test that we get at least 500 records
    assert i > 0


def test_search_records_json():
    i = 0

    for i, record in enumerate(make_request(format="json").each_record()):
        assert "primaryAccession" in record
        assert "sequence" in record

    # Test that we get many records
    assert i > 500


def test_search_records_tsv():
    i = 0

    for i, record in enumerate(make_request(format="tsv").each_record()):
        assert int(record["Length"]) >= 2500

    # Test that we get many records
    assert i > 500


def test_search_records_xml():
    i = 0

    for i, record in enumerate(make_request(format="xml").each_record()):
        seq = record.find("{http://uniprot.org/uniprot}sequence")
        assert int(seq.attrib["length"]) >= 2500

    # Test that we get many records
    assert i > 500


def test_search_records_list():
    i = 0

    for i, record in enumerate(make_request(format="list").each_record()):
        assert isinstance(record, str)

    # Test that we get many records
    assert i > 500


def test_main_example():
    """
    Validate the readme example
    """
    for record in UniprotkbSearch(
        query={"and_": [{"organelle": "chloroplast"}, {"length": (5000, "*")}]},
        fields=["length", "gene_names"],
    ).each_record():
        assert isinstance(record, dict)
        assert set(record.keys()) == {"primaryAccession", "genes", "sequence"}
        assert record["sequence"]["length"] > 5000


def test_date_field():
    """
    Validate a date field
    """
    records = list(
        UniprotkbSearch(
            query={
                "date_created": (date(2022, 1, 18), date(2022, 1, 19)),
                "organism_id": "9606",
            },
            fields=["date_created", "protein_name"],
        ).each_record()
    )
    assert len(records) == 544


def test_uniref():
    # This is an example from the uniprot website
    assert (
        len(
            list(
                UnirefSearch(
                    query={
                        "and_": [
                            {
                                "uniprot_id": "q9h9k5",
                            },
                            {"identity": "1.0"},
                        ]
                    }
                ).each_record()
            )
        )
        == 1
    )


def test_uniprac():
    # This is an example from the uniprot website
    assert (
        len(
            list(
                UnirefSearch(
                    query={
                        "and_": [
                            {
                                "uniprot_id": "q9h9k5",
                            },
                            {"identity": "1.0"},
                        ]
                    }
                ).each_record()
            )
        )
        == 1
    )
