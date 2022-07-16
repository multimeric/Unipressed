from uniprot_rest import Search


def make_request(**kwargs) -> Search:
    defaults = dict(
        query="taxonomy_id:9606 AND length:[2500 TO *]",
        dataset="uniprotkb",
        format="json",
        fields=["length"],
    )
    defaults.update(kwargs)
    return Search(**defaults)


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
        assert 'primaryAccession' in record
        assert 'sequence' in record

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
        seq = record.find("{*}sequence")
        assert int(seq.attrib["length"]) >= 2500

    # Test that we get many records
    assert i > 500


def test_search_records_list():
    i = 0

    for i, record in enumerate(make_request(format="list").each_record()):
        assert isinstance(record, str)

    # Test that we get many records
    assert i > 500
