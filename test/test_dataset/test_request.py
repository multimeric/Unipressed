from datetime import date

import pytest

from unipressed import *
from unipressed.dataset.search import Search


def make_request(**kwargs) -> Search:
    defaults = dict(
        query="taxonomy_id:9606 AND length:[2500 TO *]",
        dataset="uniprotkb",
        format="json",
        fields=["length"],
    )
    defaults.update(kwargs)
    return Search(**defaults)  # type: ignore


def assert_valid_request(search: Search):
    next(iter(search.each_response())).raise_for_status()


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
    from unipressed import UniprotkbClient

    for record in UniprotkbClient.search(
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
        UniprotkbClient.search(
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
                UnirefClient.search(
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


def test_uniparc():
    # This is an example from the uniprot website
    assert_valid_request(
        UniparcClient.search(query={"and_": [{"database": "RefSeq"}, "APP"]})
    )


def test_proteomes():
    next(
        iter(
            ProteomesClient.search(
                query={"and_": [{"busco": (90, 100)}, {"proteome_type": "1"}]}
            ).each_response()
        )
    ).raise_for_status()


def test_taxonomy():
    assert_valid_request(
        TaxonomyClient.search(query={"and_": [{"rank": "FAMILY"}, "hominidae"]})
    )


def test_keywords():
    assert_valid_request(
        KeywordsClient.search(
            query={"and_": [{"category": "technical_term"}, {"name": "food"}]}
        )
    )


def test_citations():
    assert_valid_request(
        CitationsClient.search(query={"and_": [{"published": "2022"}, "COVID-19"]})
    )


def test_diseases():
    assert_valid_request(DiseasesClient.search(query={"id": "DI-00001"}))


def test_cross_refs():
    assert_valid_request(
        DatabaseClient.search(
            query={
                # Find all databases that contain the word "Gene"
                "name": "Gene"
            }
        )
    )


def test_subcellular():
    assert_valid_request(
        LocationsClient.search(
            query={
                # Find the location with id SL-0011
                "id": "SL-0011"
            }
        )
    )


def test_unirule():
    assert_valid_request(
        UniruleClient.search(
            query={"and_": [{"taxonomy": "fungi"}, {"protein_name": "glucanase"}]}
        )
    )


def test_arba():
    assert_valid_request(
        ArbaClient.search(
            query={"and_": [{"taxonomy": "chloroflexi"}, {"keyword": "metal-binding"}]}
        )
    )

@pytest.mark.paremetrize("include_isoform,expected_result_count", [(True, 2), (False, 1)])
def test_UnirefClient_search_include_isoform(include_isoform: bool, expected_result_count: int):
    records = list(
        UniprotkbClient.search(
            query={
                "accession": "Q8WU66",
                "organism_id": "9606",
            },
            fields=["date_created", "protein_name"],
            include_isoform=include_isoform,
        ).each_record()
    )
    assert len(records) == expected_result_count
