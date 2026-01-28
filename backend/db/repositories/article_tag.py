from sqlalchemy.orm import Session
from ..models import ArticleTag


class ArticleTagRepository:
    def __init__(self, session: Session):
        self.session = session

    def get(self, article_id: int, tag_id: int) -> ArticleTag | None:
        article_tag = self.session.get(ArticleTag, (article_id, tag_id))
        return article_tag
    
    def add(self, new_article_tag: ArticleTag) -> None:
        self.session.add(new_article_tag)
        self.session.flush()

    def delete(self, article_tag: ArticleTag) -> None:
        self.session.delete(article_tag)
        self.session.flush()
