from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, text
from sqlalchemy.orm import relationship
from ..database import Base


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

    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(300), nullable=False)
    normalized_title = Column(String(300), nullable=False)
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

    def __repr__(self) -> str:
        return f"<Article(id = {self.id}, title = {self.title}, url = {self.url})>"