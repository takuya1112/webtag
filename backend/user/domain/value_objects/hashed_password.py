from dataclasses import dataclass

from core.constants import UserConfig
from core.logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class HashedPassword:
    value: str

    def __post_init__(self):
        if not self.value:
            logger.warning("HashedPassword must be filled")
            raise ValueError("HashedPassword must be filled")

        max_len = UserConfig.DB_PASSWORD_LENGTH_MAX
        if len(self.value) > max_len:
            logger.warning("HashedPassword at most %d characters", max_len)
            raise ValueError("HashedPassword is too long")

    def __str__(self) -> str:
        return "***HASHED***"

    def __repr__(self) -> str:
        return "HashedPassword(***)"
