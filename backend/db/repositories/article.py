from sqlalchemy import func
from sqlalchemy.orm import Session
from ..models import Article


class ArticleRepository:
    def __init__(self, session: Session):
        self.session = session

    def get(self, article_id: int) -> Article | None:
        return self.session.get(Article, article_id)
    
    def get_all(self) -> list[Article]:
        return self.session.query(Article).filter(Article.is_deleted.is_(False)).all()
    
    def add(self, article: Article) -> None:
        self.session.add(article)
        self.session.flush()

    def soft_delete(self, article: Article) -> None:
        article.is_deleted = True
        article.deleted_at = func.now()

    def soft_delete_all(self) -> None:
        now = func.now()
        self.session.query(Article)\
            .filter(Article.is_deleted.is_(False))\
            .update(
                {Article.is_deleted: True, Article.deleted_at: now}, 
                synchronize_session=False
            )

    def update(
            self, 
            *,
            article: Article,  
            title: str | None = None, 
            normalized_title: str | None = None,
            url: str | None = None
        ) -> None:
        article.title = title
        article.normalized_title = normalized_title
        article.url = url
        self.session.flush()