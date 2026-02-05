from sqlalchemy import (
    Column, Integer, String, Index, ForeignKey, func 
) 
from sqlalchemy.orm import relationship
from ..database import Base


# | Column  | Type         | Constraints  | Description |
# | ------- | ------------ | ------------ | ----------- |
# | id      | INTEGER      | PK           | Tag id      |
# | name    | VARCHAR(300) | NOT NULL     | Tag name    |
# | user_id | INTEGER      | FK, NOT NULL | user.id     |

class Tag(Base):
    """Tag Model

    Attributes:
        id: The Primary Key of the article.
        name: The name of the tag.
    """

    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    name = Column(String(300), nullable=False)

    articles = relationship("Article", secondary="article_tag", back_populates="tags") 
    users = relationship("User", back_populates="tags")

    __table_args__ = (
        Index(
            "ix_tag_user_name_lower",
            user_id,
            func.lower(name),
        ),
    )

    def __repr__(self) -> str:
        return f"<Tag(id = {self.id}, name = {self.name})>"
    