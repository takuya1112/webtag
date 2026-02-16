from core.constants import TagConfig
from shared.infrastructure.base import Base
from sqlalchemy import Column, ForeignKey, Index, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class TagModel(Base):
    """Tag Model"""

    __tablename__ = "tags"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    name = Column(String(TagConfig.DB_NAME_LENGTH_MAX), nullable=False)

    user = relationship("UserModel", back_populates="tags")
    articles = relationship(
        "ArticleModel",
        secondary="article_tag",
        back_populates="tags",
    )

    __table_args__ = (
        Index(
            "ix_tag_user_name_lower",
            user_id,
            func.lower(name),
        ),
    )
