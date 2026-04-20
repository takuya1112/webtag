from typing import Protocol, runtime_checkable

from .entity import ArticleEntity
from .value_objects import ArticleId


@runtime_checkable
class ArticleRepository(Protocol):
    """Article repository interface"""

    def add(self, article: ArticleEntity) -> None:
        """Add an article

        Args:
            article (ArticleEntity): The article to add
        """

    def soft_delete(self, article: ArticleEntity) -> None:
        """Soft delete an article

        Args:
            article (ArticleEntity): The article to soft delete
        """

    def soft_delete_all(self) -> None:
        """Soft delete all article"""

    def search_by_keywords(self, keywords: list[str]) -> list[ArticleEntity]:
        """Search articles by keywords"""

    def find_by_id(self, article_id: ArticleId) -> ArticleEntity | None:
        """Find a article by article id"""

    def find_all(self) -> list[ArticleEntity]:
        """Find all article"""

    def update(self, article: ArticleEntity) -> None:
        """Update an article

        Args:
            article (ArticleEntity): The article to update
        """

    def restore(self, article: ArticleEntity) -> None:
        """Restore an deleted article

        Args:
            article (ArticleEntity): The deleted article to restore
        """

    def restore_all(self) -> int:
        """Restore all deleted article"""

    def hard_delete_deleted(self, article: ArticleEntity) -> None:
        """Hard delete a deleted article

        Args:
            article (ArticleEntity): The deleted article to hard delete
        """

    def hard_delete_all_deleted(self) -> None:
        """Hard delete all deleted article"""

    def find_deleted_by_id(self, article_id: ArticleId) -> ArticleEntity | None:
        """Find a deleted article by article id"""

    def find_all_deleted(self) -> list[ArticleEntity]:
        """Find all deleted article"""

    def delete_outdated_articles(self) -> None:
        """Delete outdated deleted articles"""
