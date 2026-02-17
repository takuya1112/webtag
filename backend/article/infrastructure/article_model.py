from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from core.constants import ArticleConfig
from shared.infrastructure.base import Base
from sqlalchemy import DateTime, ForeignKey, Index, String, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from tag.infrastructure.model import TagModel
    from user.infrastructure.model import UserModel


class ArticleModel(Base):
    """Article Model"""

    __tablename__ = "articles"
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
    )
    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    title: Mapped[str] = mapped_column(
        String(ArticleConfig.DB_TITLE_LENGTH_MAX),
    )
    url: Mapped[str] = mapped_column(
        String(ArticleConfig.DB_URL_LENGTH_MAX),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    user: Mapped[UserModel] = relationship(
        back_populates="articles",
    )
    tags: Mapped[list[TagModel]] = relationship(
        secondary="article_tag",
        back_populates="articles",
        passive_deletes=True,
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
