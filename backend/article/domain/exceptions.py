from typing import Any


class ArticleDomainError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class ArticleAlreadyDeleted(ArticleDomainError):
    pass


class ArticleNotDeleted(ArticleDomainError):
    pass


class ArticleIdInvalidError(ArticleDomainError):
    pass


class ArticleCreatedAtInvalidError(ArticleDomainError):
    pass


class ArticleUpdatedAtInvalidError(ArticleDomainError):
    pass


class ArticleDeletedAtInvalidError(ArticleDomainError):
    pass
