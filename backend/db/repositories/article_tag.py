from sqlalchemy.orm import Session
from ..models import ArticleTag


class ArticleTagRepository:
    def __init__(self, session: Session):
        self.session = session

    def get(self, article_id: int, tag_id: int) -> ArticleTag | None:
        return self.session.get(ArticleTag, (article_id, tag_id))
    
    def add(self, new_article_tag: ArticleTag) -> None:
        self.session.add(new_article_tag)

    def delete(self, article_tag: ArticleTag) -> None:
        self.session.delete(article_tag)
