from dataclasses import dataclass

from core.logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class UserId:
    """User id Value object

    Raises:
        ValueError: raise if user id is negative
    """

    value: int

    def __post_init__(self):
        if self.value <= 0:
            logger.warning(f"Invalid UserId: {self.value}")
            raise ValueError("UserId must be positive")

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"UserId('{self.value}')"

    def __int__(self) -> int:
        return self.value
