import re
from dataclasses import dataclass

from core.constants import UserConfig
from core.logging import get_logger

logger = get_logger(__name__)

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self):
        if not self.value:
            logger.warning("Email must be filled")
            raise ValueError("Email must be filled")

        max_len = UserConfig.DB_EMAIL_LENGTH_MAX
        if len(self.value) > max_len:
            logger.warning("Email at most %d characters", max_len)
            raise ValueError("Email is too long")

        if not EMAIL_REGEX.match(self.value):
            logger.warning("Invalid email format: %s", self.value)
            raise ValueError("Invalid email")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"Email('{self.value}')"

    @property
    def domain(self) -> str:
        return self.value.split("@")[1]

    @property
    def local_part(self) -> str:
        return self.value.split("@")[0]
