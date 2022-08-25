from typing import Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict, TypeGuard


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
    autoCompleteQueryTerm: NotRequired[str]


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


def is_general(field: UniprotConcreteLeafField) -> TypeGuard[UniprotGeneralField]:
    return field["fieldType"] == "general"


def is_enum(field: UniprotConcreteLeafField) -> TypeGuard[UniprotEnumField]:
    return field["fieldType"] == "general"
