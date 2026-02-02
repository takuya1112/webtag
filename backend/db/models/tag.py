from sqlalchemy import Column, Integer, String, func, Index
from sqlalchemy.orm import relationship
from ..database import Base


class Tag(Base):
    """Tag Model

    Attributes:
        id: The Primary Key of the article.
        name: Tag name of the tag.
    """

    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), nullable=False)

    articles = relationship("Article", secondary="article_tag", back_populates="tags") 

    __table_args__ = (
        Index(
            "idx_tag_name_lower",
            func.lower(name)
        ),
    )

    def __repr__(self) -> str:
        return f"<Tag(id = {self.id}, name = {self.name})>"
    