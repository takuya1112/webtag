from dataclasses import dataclass
from uuid import UUID

from ..exceptions import InvalidUuidError


@dataclass(frozen=True)
class AppUuid:
    """AppUuid value objects

    Raises:
        InvalidUuidError: if not UUID objects
    """

    value: UUID

    def __post_init__(self):
        if not isinstance(self.value, UUID):
            raise InvalidUuidError()

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}')"

    def __eq__(self, other: "AppUuid | UUID") -> bool:
        if isinstance(other, AppUuid):
            return self.value == other.value
        return self.value == other
