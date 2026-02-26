from dataclasses import dataclass

from shared.domain.value_objects import AwareDatetime
from user.domain.value_objects import UserId

from ..exceptions import ArticleAlreadyDeleted, ArticleNotDeleted
from .value_objects import URL, ArticleId, ArticleTitle


@dataclass
class ArticleEntity:
    id: ArticleId
    user_id: UserId
    title: ArticleTitle
    url: URL
    created_at: AwareDatetime
    updated_at: AwareDatetime
    deleted_at: AwareDatetime | None = None

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None

    def restore(self, now: AwareDatetime) -> None:
        if not self.is_deleted:
            raise ArticleNotDeleted()
        self.deleted_at = None
        self.updated_at = now

    def soft_delete(self, now: AwareDatetime) -> None:
        if self.is_deleted:
            raise ArticleAlreadyDeleted()
        self.deleted_at = now
        self.updated_at = now

    def change_title(self, new_title: ArticleTitle, now: AwareDatetime) -> None:
        if self.is_deleted:
            raise ArticleAlreadyDeleted()
        self.title = new_title
        self.updated_at = now

    def change_url(self, new_url: URL, now: AwareDatetime) -> None:
        if self.is_deleted:
            raise ArticleAlreadyDeleted()
        self.url = new_url
        self.updated_at = now
