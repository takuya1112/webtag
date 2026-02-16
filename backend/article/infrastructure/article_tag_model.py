from shared.infrastructure.base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class ArticleTagModel(Base):
    __tablename__ = "article_tag"
    article_id = Column(
        UUID(as_uuid=True),
        ForeignKey("articles.id", ondelete="CASCADE"),
        primary_key=True,
    )
    tag_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tags.id", ondelete="CASCADE"),
        primary_key=True,
    )
