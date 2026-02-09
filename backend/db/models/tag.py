from sqlalchemy import (
    Column, BigInteger, String, Index, ForeignKey, func 
) 
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from ..session import Base
from core.constants import TagConfig


class Tag(Base):
    """Tag Model

    Attributes:
        id: The Primary Key of the article.
        name: The name of the tag.
    """

    __tablename__ = 'tags'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    public_id = Column(UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(TagConfig.DB_NAME_LENGTH_MAX), nullable=False)

    articles = relationship("Article", secondary="article_tag", back_populates="tags") 
    user = relationship("User", back_populates="tags")

    __table_args__ = (
        Index(
            "ix_tag_user_name_lower",
            user_id,
            func.lower(name),
        ),
    )