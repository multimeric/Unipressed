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


class UniprotGroupField(UniprotBaseSearchField):
    itemType: Literal["group"]
    items: list["UniprotSearchField"]


class UniprotSiblingField(UniprotBaseSearchField):
    itemType: Literal["sibling_group"]
    siblings: list["UniprotSearchField"]


class UniprotLeafField(UniprotBaseSearchField):
    itemType: Literal["single"]
    term: str
    example: NotRequired[str]
    regex: NotRequired[str]


class UniprotEnumField(UniprotLeafField):
    fieldType: Literal["general"]
    dataType: Literal["enum"]
    values: list[UniprotEnumEntry]


class UniprotGeneralField(UniprotLeafField):
    fieldType: Literal["general", "range"]
    dataType: Literal["string", "integer", "date", "boolean"]


class UniprotEvidenceField(UniprotLeafField):
    fieldType: Literal["evidence"]
    dataType: Literal["string", "integer", "date", "boolean"]
    evidenceGroups: list[EvidenceGroup]


UniprotConcreteLeafField: TypeAlias = Union[
    UniprotEnumField, UniprotGeneralField, UniprotEvidenceField
]

UniprotSearchField: TypeAlias = Union[
    UniprotConcreteLeafField, UniprotGroupField, UniprotSiblingField
]
