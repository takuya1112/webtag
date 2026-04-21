from typing import Any


class ArticleDomainError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }


class ArticleAlreadyDeleted(ArticleDomainError):
    pass


class ArticleNotDeleted(ArticleDomainError):
    pass


class ArticleIdInvalidError(ArticleDomainError):
    pass


class ArticleTitleEmptyError(ArticleDomainError):
    pass


class ArticleTitleTooLongError(ArticleDomainError):
    def __init__(self, max_length: int) -> None:
        super().__init__()
        self.max_length = max_length


class ArticleUrlEmptyError(ArticleDomainError):
    pass


class ArticleUrlInvalidFormatError(ArticleDomainError):
    pass


class ArticleUrlTooLongError(ArticleDomainError):
    def __init__(self, max_length: int) -> None:
        super().__init__()
        self.max_length = max_length


class ArticleCreatedAtInvalidError(ArticleDomainError):
    pass


class ArticleUpdatedAtInvalidError(ArticleDomainError):
    pass


class ArticleDeletedAtInvalidError(ArticleDomainError):
    pass
