from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class TagSynonym(Base):
    __tablename__ = 'tag_synonym'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), unique=True, index=True, nullable=False)
    
    tags = relationship("Tag", back_populates="synonym") 

    def __repr__(self) -> str:
        return f"<TagSynonym(id = {self.id}, name = {self.name})>"