from core.logging import get_logger
from sqlalchemy import select
from sqlalchemy.orm import Session
from user.domain.value_objects import UserId

from ..domain.entity import ArticleEntity
from ..domain.value_objects import (
    URL,
    ArticleId,
    ArticleTitle,
    CreatedAt,
    DeletedAt,
    UpdatedAt,
)
from .article_model import ArticleModel

logger = get_logger(__name__)


class SQLAlchemyArticleRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, article: ArticleEntity) -> None:
        """Add an article

        Args:
            article (ArticleEntity): The article to add
        """
        model = self._to_model(article)
        self.session.add(model)
        logger.debug("Article added")

    def soft_delete(self, article: ArticleEntity) -> None:
        """Soft delete an article

        Args:
            article (ArticleEntity): The article to soft delete
        """
        pass

    def soft_delete_all(self) -> None:
        """Soft delete all article"""
        pass

    def search_by_keywords(self, keywords: list[str]) -> list[ArticleEntity]:
        """Search articles by keywords"""
        pass

    def find_by_id(self, article_id: ArticleId) -> ArticleEntity | None:
        """Find a article by article id"""
        stmt = select(ArticleModel).where(
            ArticleModel.id == article_id.value,
            ArticleModel.deleted_at.is_(None),
        )
        model = self.session.scalars(stmt).first()
        if model:
            logger.debug(
                "Article found by article id: %s",
                article_id.value,
            )
        else:
            logger.debug(
                "Article not found by article id: %s",
                article_id.value,
            )
        return self._to_entity(model) if model else None

    def find_all(self) -> list[ArticleEntity]:
        """Find all article"""
        stmt = select(ArticleModel).where(ArticleModel.deleted_at.is_(None))
        models = self.session.scalars(stmt).all()
        logger.debug("%s article found", len(models))
        return [self._to_entity(model) for model in models]

    def update(self, article: ArticleEntity) -> None:
        """Update an article

        Args:
            article (ArticleEntity): The article to update
        """
        pass

    def restore(self, article: ArticleEntity) -> None:
        """Restore an deleted article

        Args:
            article (ArticleEntity): The deleted article to restore
        """
        pass

    def restore_all(self) -> int:
        """Restore all deleted article"""
        pass

    def hard_delete_deleted(self, article: ArticleEntity) -> None:
        """Hard delete a deleted article

        Args:
            article (ArticleEntity): The deleted article to hard delete
        """
        pass

    def hard_delete_all_deleted(self) -> None:
        """Hard delete all deleted article"""
        pass

    def find_deleted_by_id(self, article_id: ArticleId) -> ArticleEntity | None:
        """Find a deleted article by article id"""
        stmt = select(ArticleModel).where(
            ArticleModel.id == article_id.value,
            ArticleModel.deleted_at.is_not(None),
        )
        model = self.session.scalars(stmt).first()
        if model:
            logger.debug(
                "Deleted article found by article id: %s",
                article_id.value,
            )
        else:
            logger.debug(
                "Deleted article not found by article id: %s",
                article_id.value,
            )
        return self._to_entity(model) if model else None

    def find_all_deleted(self) -> list[ArticleEntity]:
        """Find all deleted article"""
        stmt = select(ArticleModel).where(ArticleModel.deleted_at.is_not(None))
        models = self.session.scalars(stmt).all()
        logger.debug("%s article found", len(models))
        return [self._to_entity(model) for model in models]

    def delete_outdated_articles(self) -> None:
        """Delete outdated deleted articles"""
        pass

    def _to_entity(self, model: ArticleModel) -> ArticleEntity:
        """SQLAlchemy model -> Domain entity"""
        return ArticleEntity(
            id=ArticleId(model.id),
            user_id=UserId(model.user_id),
            title=ArticleTitle(model.title),
            url=URL(model.url),
            created_at=CreatedAt(model.created_at),
            updated_at=UpdatedAt(model.updated_at),
            deleted_at=DeletedAt(model.deleted_at)
            if model.deleted_at
            else None,
        )

    def _to_model(self, entity: ArticleEntity) -> ArticleModel:
        """Domain entity -> SQLAlchemy model"""
        return ArticleModel(
            id=entity.id.value,
            user_id=entity.user_id.value,
            title=entity.title.value,
            url=entity.url.value,
            created_at=entity.created_at.value,
            updated_at=entity.updated_at.value,
            deleted_at=entity.deleted_at.value if entity.deleted_at else None,
        )
