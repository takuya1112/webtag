from sqlalchemy import (
    Column, BigInteger, String, Boolean, DateTime, Index,
    ForeignKey, text, func
) 
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from ..core import Base


class Article(Base):
    """Article Model

    Attributes:
        id: The Primary Key of the article.
        title: The title of the article.
        url: The URL of the article.
        created_at: The timestamp when the article was created.
        updated_at: The timestamp when the article was last updated.
        is_deleted: A flag indicating if the article is soft-deleted.
        deleted_at: The timestamp when the article was soft-deleted
    """

    __tablename__ = 'articles'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    public_id = Column(UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(300), nullable=False)
    url = Column(String(2083), nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
    is_deleted = Column(Boolean, server_default=text("false"), nullable=False)
    deleted_at = Column(DateTime(timezone=True))

    tags = relationship("Tag", secondary="article_tag", back_populates="articles")
    user = relationship("User", back_populates="articles")

    __table_args__ = (
        Index(
            "ix_article_user_title_lower",
            user_id,
            func.lower(title),
            postgresql_where=(is_deleted.is_(False)),
        ),
        Index(
            "ix_article_user_created_at",
            user_id,
            created_at,
            postgresql_where=(is_deleted.is_(False)),
        ),
        Index(
            "ix_article_user_updated_at",
            user_id,
            updated_at,
            postgresql_where=(is_deleted.is_(False)),
        ),
        Index(
            "ix_article_user_deleted_at",
            user_id,
            deleted_at,
            postgresql_where=(is_deleted.is_(True)),
        ),
    )