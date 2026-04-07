from typing import Protocol, runtime_checkable

from .entity import ArticleEntity


@runtime_checkable
class ArticleRepository(Protocol):
    """Article repository interface"""

    def add(self, article: ArticleEntity) -> None:
        """Add a article

        Args:
            article (ArticleEntity): The article to add
        """

    def soft_delete(self, article: ArticleEntity) -> None:
        """Soft delete a article

        Args:
            article (ArticleEntity): The article to soft delete
        """

    def update(self, article: ArticleEntity) -> None:
        """Update a article

        Args:
            article (ArticleEntity): The article to update
        """
