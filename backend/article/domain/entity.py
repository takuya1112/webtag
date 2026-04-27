from dataclasses import dataclass

from user.domain.value_objects import UserId

from .exceptions import ArticleAlreadyDeletedError, ArticleNotDeletedError
from .value_objects import (
    URL,
    ArticleId,
    ArticleTitle,
    CreatedAt,
    DeletedAt,
    UpdatedAt,
)


@dataclass
class ArticleEntity:
    id: ArticleId
    user_id: UserId
    title: ArticleTitle
    url: URL
    created_at: CreatedAt
    updated_at: UpdatedAt
    deleted_at: DeletedAt | None = None

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None

    def restore(self, updated_at: UpdatedAt) -> None:
        if not self.is_deleted:
            raise ArticleNotDeletedError()
        self.deleted_at = None
        self.updated_at = updated_at

    def soft_delete(self, deleted_at: DeletedAt, updated_at: UpdatedAt) -> None:
        if self.is_deleted:
            raise ArticleAlreadyDeletedError()
        self.deleted_at = deleted_at
        self.updated_at = updated_at

    def change_title(
        self,
        new_title: ArticleTitle,
        updated_at: UpdatedAt,
    ) -> None:
        if self.is_deleted:
            raise ArticleAlreadyDeletedError()
        self.title = new_title
        self.updated_at = updated_at

    def change_url(self, new_url: URL, updated_at: UpdatedAt) -> None:
        if self.is_deleted:
            raise ArticleAlreadyDeletedError()
        self.url = new_url
        self.updated_at = updated_at
