from uniprot_rest import Search, serialize_query


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

def test_serialize_basic_query():
    assert serialize_query({
        "a": 3
    }) == "a:3"

def test_serialize_not_query():
    assert serialize_query({
        "not": {
            "a": 3
        }
    }) == "NOT a:3"


def test_serialize_and():
    assert serialize_query({
        "and": [
            {"a": 3},
            {"b": 4}
        ]
    }) == "a:3 AND b:4"


def test_serialize_or():
    assert serialize_query({
        "or": [
            {"a": 3},
            {"b": 4},
        ]
    }) == "a:3 OR b:4"


def test_serialize_and_or():
    assert serialize_query({
        "or": [
            {"a": 3},
            {
                "and": [
                    {"b": 4},
                    {"c": 5},
                ]
            }
        ]
    }) == "a:3 OR (b:4 AND c:5)"

def test_serialize_and_not():
    assert serialize_query({
        "or": [
            {"a": 3},
            {
                "not": {
                    "and": [
                        {"b": 4},
                        {"c": 5},
                    ]
                }
            }
        ]
    }) == "a:3 OR (NOT (b:4 AND c:5))"