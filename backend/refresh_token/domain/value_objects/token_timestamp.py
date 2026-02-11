from dataclasses import dataclass
from datetime import datetime

from core import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class TokenTimestamp:
    """Token timestamp value object

    Raises:
        ValueError: raise if value is not timezone-aware
    """

    value: datetime

    def __post_init__(self):
        if self.value.tzinfo is None:
            logger.warning("TokenTimestamp must be timezone-aware")
            raise ValueError("TokenTimestamp must be timezone-aware")

    def __str__(self):
        return self.value.isoformat()

    def __le__(self, other: datetime) -> bool:
        return self.value <= other

    def __lt__(self, other: datetime) -> bool:
        return self.value < other

    def __ge__(self, other: datetime) -> bool:
        return self.value >= other

    def __gt__(self, other: datetime) -> bool:
        return self.value > other
