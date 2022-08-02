from typing import Type, get_args, get_type_hints
import pytest
from uniprot_rest.base import Search, serialize_query
from datetime import date

import uniprot_rest.types


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

def test_serialize_implicit_and():
    assert serialize_query({
        "a": 3,
        "b": 4,
        "c": 5,
    }) == "a:3 AND b:4 AND c:5"

def test_serialize_not_query():
    assert serialize_query({
        "not_": {
            "a": 3
        }
    }) == "NOT a:3"


def test_serialize_and():
    assert serialize_query({
        "and_": [
            {"a": 3},
            {"b": 4}
        ]
    }) == "a:3 AND b:4"


def test_serialize_or():
    assert serialize_query({
        "or_": [
            {"a": 3},
            {"b": 4},
        ]
    }) == "a:3 OR b:4"


def test_serialize_and_or():
    assert serialize_query({
        "or_": [
            {"a": 3},
            {
                "and_": [
                    {"b": 4},
                    {"c": 5},
                ]
            }
        ]
    }) == "a:3 OR (b:4 AND c:5)"

def test_serialize_and_not():
    assert serialize_query({
        "or_": [
            {"a": 3},
            {
                "not_": {
                    "and_": [
                        {"b": 4},
                        {"c": 5},
                    ]
                }
            }
        ]
    }) == "a:3 OR (NOT (b:4 AND c:5))"


def test_serialize_int_range():
    assert serialize_query((1, 3)) == "[1 TO 3]"

def test_serialize_half_int_range():
    assert serialize_query((1, "*")) == "[1 TO *]"

def test_serialize_nested_range():
    assert serialize_query({"and_": [
        {"a": (1, 3)},
        {"b": (2, "*")},
    ]}) == "a:[1 TO 3] AND b:[2 TO *]"

def test_serialize_date_range():
    assert serialize_query((date(day=1, month=2, year=3000), date(day=2, month=2, year=3000))) == "[3000-02-01 TO 3000-02-02]"

def test_serialize_bool():
    assert serialize_query(True) == "true"

@pytest.mark.parametrize([
    "client"
], [[it] for it in uniprot_rest.types.all_clients])
def test_valid_query_fields(client: Type[Search]):
    """
    Test that all the query fields defined by our schemas are accepted by Uniprot
    """
    query = {}
    for query_field in get_type_hints(client)["query"].__optional_keys__:
        if query_field not in {"and_", "or_", "not_"}:
            query[query_field] = "foo"
    response = next(iter(client( query=query    ).each_response()))

    # Only raise an error if the request failed, and then only if because we provided an invalid field
    # We aren't interested in other types of validation error in this test
    if response.status_code != 200:
        for warning in response.json()["messages"]:
            assert "is not a valid search field" not in warning

@pytest.mark.parametrize([
    "client"
], [[it] for it in uniprot_rest.types.all_clients])
def test_valid_return_fields(client: Type[Search]):
    """
    Test that all the return fields defined by our schemas are accepted by Uniprot
    """
    # We get a response such as "Invalid fields parameter value 'foo'" with a 400 status code if we provide an invalid field
    response = next(iter(client( query="ThisQueryShouldReturnNoResults", fields=get_args(get_type_hints(client)["fields"])).each_response()))
    response.raise_for_status()