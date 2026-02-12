from core.session import Base
from sqlalchemy import BigInteger, Column, ForeignKey


class ArticleTag(Base):
    """ArticleTag の情報を管理するモデル

    Attributes:
        article_id: article.id (Primary Key, Foreign Key)
        tag_id: tag.id (Primary Key, Foreign Key)
    """

    __tablename__ = "article_tag"
    article_id = Column(
        BigInteger,
        ForeignKey("articles.id", ondelete="CASCADE"),
        primary_key=True,
    )
    tag_id = Column(
        BigInteger,
        ForeignKey("tags.id", ondelete="CASCADE"),
        primary_key=True,
    )
