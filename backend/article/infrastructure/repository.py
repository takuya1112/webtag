from core.logging import get_logger
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
        """Add a article

        Args:
            article (ArticleEntity): The article to add
        """
        model = self._to_model(article)
        self.session.add(model)
        logger.debug("Article added")

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
