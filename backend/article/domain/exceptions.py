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


class ArticleTitleEmptyError(ArticleDomainError):
    pass


class ArticleTitleTooLongError(ArticleDomainError):
    pass


class ArticleUrlEmptyError(ArticleDomainError):
    pass


class ArticleUrlInvalidFormatError(ArticleDomainError):
    pass


class ArticleUrlTooLongError(ArticleDomainError):
    pass


class ArticleCreatedAtInvalidError(ArticleDomainError):
    pass


class ArticleUpdatedAtInvalidError(ArticleDomainError):
    pass


class ArticleDeletedAtInvalidError(ArticleDomainError):
    pass
