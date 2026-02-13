from dataclasses import dataclass

from core.logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class HashedToken:
    """Hashed token value object

    Raises:
        ValueError: raise if hashed token is empty
    """

    value: str

    def __post_init__(self):
        if not self.value:
            logger.warning("HashedToken must be filled")
            raise ValueError("HashedToken must be filled")

    def __str__(self):
        return self.value
