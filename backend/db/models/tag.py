from sqlalchemy import Column, Integer, String, event
from sqlalchemy.orm import relationship
from ..database import Base

class Tag(Base):
    """Tag Model

    Attributes:
        id: The Primary Key of the article.
        name: Tag name of the tag.
        name_lower: Lowercase name for case-insensitive search.
    """

    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), nullable=False)
    name_lower = Column(String(300), nullable=False)

    articles = relationship("Article", secondary="article_tag", back_populates="tags") 

    def __repr__(self) -> str:
        return f"<Tag(id = {self.id}, name = {self.name})>"
    
@event.listens_for(Tag, "before_insert")
@event.listens_for(Tag, "before_update")
def lowercase_name(mapper, connection, target):
    if target.name:
        target.name_lower = target.name.lower()