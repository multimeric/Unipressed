from typing import Any, Mapping, TypeVar

QueryType = TypeVar("QueryType")
JsonResultType = TypeVar("JsonResultType", bound=Mapping[str, Any])
FieldsType = TypeVar("FieldsType", bound=str)
FormatType = TypeVar("FormatType", bound=str)
