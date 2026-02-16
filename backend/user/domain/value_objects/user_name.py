from dataclasses import dataclass

from core.constants import UserConfig
from core.logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class UserName:
    """User name value object

    Raises:
        ValueError: raise if user name is empty
        ValueError: raise if user name is too short
        ValueError: raise if user name is too long
    """

    value: str

    def __post_init__(self):
        object.__setattr__(self, "value", self.value.strip())

        if not self.value:
            logger.warning("UserName must be filled")
            raise ValueError("UserName must be filled")

        min_len = UserConfig.NAME_LENGTH_MIN
        max_len = UserConfig.NAME_LENGTH_MAX
        if len(self.value) < min_len:
            logger.warning("UserName at least %d characters", min_len)
            raise ValueError("UserName is too short")

        if len(self.value) > max_len:
            logger.warning("UserName at most %d characters", max_len)
            raise ValueError("UserName is too long")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"UserName('{self.value}')"
