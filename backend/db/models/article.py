from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from ..database import Base


class Article(Base):
    """
    Article の情報を管理するモデル

    Attribute:
        id: 記事のID (Primary Key)
        title: 記事のタイトル (最大300文字)
        url: 記事のURL (最大2083文字)
        created_at: 作成日時が自動で挿入される
        edited_at: 最終編集日時が自動で更新される
    """

    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    url = Column(String(2083), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    edited_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)

    tags = relationship("Tag", secondary="article_tag", back_populates="articles")

    def __repr__(self) -> str:
        """ デバッグ用 """
        return f"<Aricle(id = {self.id}, title = {self.title})>"