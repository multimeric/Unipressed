from datetime import date

from unipressed.base import serialize_query


def test_serialize_basic_query():
    assert serialize_query({"a": 3}) == "a:3"


def test_serialize_implicit_and():
    assert (
        serialize_query(
            {
                "a": 3,
                "b": 4,
                "c": 5,
            }
        )
        == "a:3 AND b:4 AND c:5"
    )


def test_serialize_not_query():
    assert serialize_query({"not_": {"a": 3}}) == "NOT a:3"


def test_serialize_and():
    assert serialize_query({"and_": [{"a": 3}, {"b": 4}]}) == "a:3 AND b:4"


def test_serialize_or():
    assert (
        serialize_query(
            {
                "or_": [
                    {"a": 3},
                    {"b": 4},
                ]
            }
        )
        == "a:3 OR b:4"
    )


def test_serialize_and_or():
    assert (
        serialize_query(
            {
                "or_": [
                    {"a": 3},
                    {
                        "and_": [
                            {"b": 4},
                            {"c": 5},
                        ]
                    },
                ]
            }
        )
        == "a:3 OR (b:4 AND c:5)"
    )


def test_serialize_and_not():
    assert (
        serialize_query(
            {
                "or_": [
                    {"a": 3},
                    {
                        "not_": {
                            "and_": [
                                {"b": 4},
                                {"c": 5},
                            ]
                        }
                    },
                ]
            }
        )
        == "a:3 OR (NOT (b:4 AND c:5))"
    )


def test_serialize_int_range():
    assert serialize_query((1, 3)) == "[1 TO 3]"


def test_serialize_half_int_range():
    assert serialize_query((1, "*")) == "[1 TO *]"


def test_serialize_nested_range():
    assert (
        serialize_query(
            {
                "and_": [
                    {"a": (1, 3)},
                    {"b": (2, "*")},
                ]
            }
        )
        == "a:[1 TO 3] AND b:[2 TO *]"
    )


def test_serialize_date_range():
    assert (
        serialize_query(
            (date(day=1, month=2, year=3000), date(day=2, month=2, year=3000))
        )
        == "[3000-02-01 TO 3000-02-02]"
    )


def test_serialize_bool():
    assert serialize_query(True) == "true"
