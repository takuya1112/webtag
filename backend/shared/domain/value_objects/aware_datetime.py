from dataclasses import dataclass
from datetime import datetime

from core.logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class AwareDatetime:
    """Datetime value object

    Raises:
        ValueError: raise if value is not timezone-aware
    """

    value: datetime

    def __post_init__(self):
        if self.value.tzinfo is None:
            logger.warning("AwareDatetime must be timezone-aware")
            raise ValueError("AwareDatetime must be timezone-aware")

    def __str__(self) -> str:
        return self.value.isoformat()

    def __repr__(self) -> str:
        return f"AwareDatetime('{self.value.isoformat()}')"

    def __le__(self, other: "AwareDatetime | datetime") -> bool:
        if isinstance(other, AwareDatetime):
            return self.value <= other.value
        return self.value <= other

    def __lt__(self, other: "AwareDatetime | datetime") -> bool:
        if isinstance(other, AwareDatetime):
            return self.value < other.value
        return self.value < other

    def __ge__(self, other: "AwareDatetime | datetime") -> bool:
        if isinstance(other, AwareDatetime):
            return self.value >= other.value
        return self.value >= other

    def __gt__(self, other: "AwareDatetime | datetime") -> bool:
        if isinstance(other, AwareDatetime):
            return self.value > other.value
        return self.value > other

    def __eq__(self, other: "AwareDatetime | datetime") -> bool:
        if isinstance(other, AwareDatetime):
            return self.value == other.value
        return self.value == other
