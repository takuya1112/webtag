from dataclasses import dataclass

from core.constants import ArticleConfig

from ..exceptions import ArticleTitleEmptyError, ArticleTitleTooLongError


@dataclass(frozen=True)
class ArticleTitle:
    value: str

    def __post_init__(self):
        object.__setattr__(self, "value", self.value.strip())

        if not self.value:
            raise ArticleTitleEmptyError() from None

        max_len = ArticleConfig.TITLE_LENGTH_MAX

        if len(self.value) > max_len:
            raise ArticleTitleTooLongError(max_len) from None

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"ArticleTitle('{self.value}')"
