from dataclasses import dataclass
from uuid import UUID

from core.logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class PublicId:
    """Public id value objects

    Raises:
        ValueError: if not UUID objects
    """

    value: UUID

    def __post_init__(self):
        if not isinstance(self.value, UUID):
            raise ValueError("Invalid UUID")

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"PublicId('{self.value}')"
