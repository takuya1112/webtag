from core.constants import ArticleConfig
from shared.infrastructure.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Index, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class ArticleModel(Base):
    """Article Model"""

    __tablename__ = "articles"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    title = Column(String(ArticleConfig.DB_TITLE_LENGTH_MAX), nullable=False)
    url = Column(String(ArticleConfig.DB_URL_LENGTH_MAX), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("UserModel", back_populates="articles")
    tags = relationship(
        "TagModel",
        secondary="article_tag",
        back_populates="articles",
    )

    __table_args__ = (
        Index(
            "ix_article_user_title_lower",
            user_id,
            func.lower(title),
            postgresql_where=(deleted_at.is_(None)),
        ),
        Index(
            "ix_article_user_created_at",
            user_id,
            created_at.desc(),
            postgresql_where=(deleted_at.is_(None)),
        ),
        Index(
            "ix_article_user_updated_at",
            user_id,
            updated_at.desc(),
            postgresql_where=(deleted_at.is_(None)),
        ),
        Index(
            "ix_article_user_deleted_at",
            user_id,
            deleted_at,
            postgresql_where=(deleted_at.isnot(None)),
        ),
    )
