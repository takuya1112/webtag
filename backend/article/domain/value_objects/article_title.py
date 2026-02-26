from dataclasses import dataclass

from core.constants import ArticleConfig
from core.logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class ArticleTitle:
    value: str

    def __post_init__(self):
        object.__setattr__(self, "value", self.value.strip())

        if not self.value:
            logger.warning("ArticleTitle must be filled")
            raise ValueError("ArticleTitle must be filled")

        max_len = ArticleConfig.TITLE_LENGTH_MAX

        if len(self.value) > max_len:
            logger.warning("ArticleTitle at most %d characters", max_len)
            raise ValueError("ArticleTitle is too long")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"ArticleTitle('{self.value}')"
