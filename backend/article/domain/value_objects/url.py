from dataclasses import dataclass

from core.constants import ArticleConfig
from core.logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class URL:
    value: str

    def __post_init__(self):
        object.__setattr__(self, "value", self.value.strip())

        if not self.value:
            logger.warning("URL must be filled")
            raise ValueError("URL must be filled")

        max_len = ArticleConfig.DB_URL_LENGTH_MAX
        if len(self.value) > max_len:
            logger.warning("URL at most %d characters", max_len)
            raise ValueError("URL is too long")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"URL('{self.value}')"
