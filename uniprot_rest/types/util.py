from typing import Callable

import attr
import attrs
from dataclasses import asdict, dataclass, field
from typing import ClassVar

@dataclass
class UniprotMixin:
    field_map: ClassVar[dict] = {}

    def asdict(self) -> dict:
        """
        Converts the dataclass to dict
        """
        base = asdict(self)
        # Map the field name if we have a replacement name
        return { key: self.field_map.get(key, value) for key, value in base.items() }

