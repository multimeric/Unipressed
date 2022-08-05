from typing import Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict


class EvidenceItem(TypedDict):
    name: str
    code: str


class EvidenceGroup(TypedDict):
    groupName: str
    items: list[EvidenceItem]


class UniprotEnumEntry(TypedDict):
    name: str
    value: str


class UniprotBaseSearchField(TypedDict):
    id: str
    label: str
    itemType: Literal["single"]
    term: str
    example: NotRequired[str]
    regex: NotRequired[str]


class UniprotEnumField(UniprotBaseSearchField):
    fieldType: Literal["general"]
    dataType: Literal["enum"]
    values: list[UniprotEnumEntry]


class UniprotGeneralField(UniprotBaseSearchField):
    fieldType: Literal["general", "range"]
    dataType: Literal["string", "integer", "date", "boolean"]


class UniprotEvidenceField(UniprotBaseSearchField):
    fieldType: Literal["evidence"]
    dataType: Literal["string", "integer", "date", "boolean"]
    evidenceGroups: list[EvidenceGroup]


UniprotSearchField: TypeAlias = Union[
    UniprotEnumField, UniprotGeneralField, UniprotEvidenceField
]
