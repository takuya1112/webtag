from typing import Any


class ArticleDomainError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }


class ArticleBaseTooLongError(ArticleDomainError):
    def __init__(self, max_length: int) -> None:
        super().__init__()
        self.max_length = max_length


class ArticleAlreadyDeleted(ArticleDomainError):
    pass


class ArticleNotDeleted(ArticleDomainError):
    pass


class ArticleIdInvalidError(ArticleDomainError):
    pass


class ArticleTitleEmptyError(ArticleDomainError):
    pass


class ArticleTitleTooLongError(ArticleBaseTooLongError):
    pass


class ArticleUrlEmptyError(ArticleDomainError):
    pass


class ArticleUrlInvalidFormatError(ArticleDomainError):
    pass


class ArticleUrlTooLongError(ArticleBaseTooLongError):
    pass


class ArticleCreatedAtInvalidError(ArticleDomainError):
    pass


class ArticleUpdatedAtInvalidError(ArticleDomainError):
    pass


class ArticleDeletedAtInvalidError(ArticleDomainError):
    pass
