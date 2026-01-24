from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Tag(Base):
    """Tag の情報を管理するモデル

    Attribute:
        id: タグのID (Primary Key)
        name: タグの名前 (最大300文字)
    """

    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), nullable=False)
    name_lower = Column(String(300), nullable=False)

    articles = relationship("Article", secondary="article_tag", back_populates="tags") 

    def __repr__(self) -> str:
        """ デバッグ用 """
        return f"<Tag(id = {self.id}, name = {self.name})>"