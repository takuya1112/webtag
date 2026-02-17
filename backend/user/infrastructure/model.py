from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from core.constants import UserConfig
from shared.infrastructure.base import Base
from sqlalchemy import DateTime, Index, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from article.infrastructure.article_model import ArticleModel
    from refresh_token.infrastructure.model import RefreshTokenModel
    from tag.infrastructure.model import TagModel


class UserModel(Base):
    """User Model"""

    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(
        String(UserConfig.DB_NAME_LENGTH_MAX),
    )
    email: Mapped[str] = mapped_column(
        String(UserConfig.DB_EMAIL_LENGTH_MAX),
        unique=True,
    )
    password_hash: Mapped[str] = mapped_column(
        String(UserConfig.DB_PASSWORD_LENGTH_MAX),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )
    deactivated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    articles: Mapped[list[ArticleModel]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    tags: Mapped[list[TagModel]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    refresh_tokens: Mapped[list[RefreshTokenModel]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    __table_args__ = (
        Index(
            "ix_users_active",
            id,
            postgresql_where=(deactivated_at.is_(None)),
        ),
    )
