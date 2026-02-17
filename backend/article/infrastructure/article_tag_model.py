from uuid import UUID

from shared.infrastructure.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column


class ArticleTagModel(Base):
    """Article Tag relation Model"""

    __tablename__ = "article_tag"
    article_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("articles.id", ondelete="CASCADE"),
        primary_key=True,
    )
    tag_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("tags.id", ondelete="CASCADE"),
        primary_key=True,
    )
