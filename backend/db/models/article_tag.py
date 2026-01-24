from sqlalchemy import Column, Integer, ForeignKey
from ..database import Base

class ArticleTag(Base):
    """ArticleTag の情報を管理するモデル

    Attributes:
        article_id: article.id (Primary Key, Foreign Key)
        tag_id: tag.id (Primary Key, Foreign Key)
    """
    
    __tablename__ = 'article_tag'
    article_id = Column(Integer, ForeignKey('article.id', ondelete="CASCADE"), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id', ondelete="CASCADE"), primary_key=True)

    def __repr__(self) -> str:
        return f"<ArticleTag(article_id = {self.article_id}, tag_id = {self.tag_id})>"
    