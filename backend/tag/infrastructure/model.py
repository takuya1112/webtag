from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from core.constants import TagConfig
from shared.infrastructure.base import Base
from sqlalchemy import ForeignKey, Index, String, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from article.infrastructure.article_model import ArticleModel
    from user.infrastructure.model import UserModel


class TagModel(Base):
    """Tag Model"""

    __tablename__ = "tags"
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
    )
    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    name: Mapped[str] = mapped_column(
        String(TagConfig.DB_NAME_LENGTH_MAX),
    )

    user: Mapped[UserModel] = relationship(
        back_populates="tags",
    )
    articles: Mapped[list[ArticleModel]] = relationship(
        secondary="article_tag",
        back_populates="tags",
        passive_deletes=True,
    )

    __table_args__ = (
        Index(
            "ix_tag_user_name_lower",
            user_id,
            func.lower(name),
        ),
    )
