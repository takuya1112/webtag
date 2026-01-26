from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class TagAlias(Base):
    __tablename__ = 'tag_alias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), unique=True, index=True, nullable=False)
    
    tags = relationship("Tag", back_populates="alias") 

    def __repr__(self) -> str:
        return f"<Tag(id = {self.id}, name = {self.name})>"