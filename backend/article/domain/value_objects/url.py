from dataclasses import dataclass
from urllib.parse import urlparse

from core.constants import ArticleConfig

from ..exceptions import (
    ArticleUrlEmptyError,
    ArticleUrlInvalidFormatError,
    ArticleUrlTooLongError,
)


@dataclass(frozen=True)
class URL:
    value: str

    def __post_init__(self):
        object.__setattr__(self, "value", self.value.strip())

        if not self.value:
            raise ArticleUrlEmptyError() from None

        parsed = urlparse(self.value)
        if parsed.scheme not in ("http", "https"):
            raise ArticleUrlInvalidFormatError() from None

        max_length = ArticleConfig.DB_URL_LENGTH_MAX
        if len(self.value) > max_length:
            raise ArticleUrlTooLongError(max_length=max_length) from None

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"URL('{self.value}')"
