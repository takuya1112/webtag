from sqlalchemy import func
from sqlalchemy.orm import Session
from ..models import Article


class ArticleRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_article_or_raise(self, article_id: int) -> Article:
        article = self.session.get(Article, article_id)
        if not article or article.is_deleted:
            raise ValueError(f"Article with id {article_id} not found")
        return article
    
    def get_all(self) -> list[Article]:
        articles = self.session.query(Article).filter(Article.is_deleted.is_(False)).all()
        return articles
    
    def add(self, article: Article) -> None:
        self.session.add(article)
        self.session.flush()

    def soft_delete(self, article: Article) -> None:
        article.is_deleted = True
        article.deleted_at = func.now()
        self.session.flush()

    def soft_delete_all(self) -> int:
        now = func.now()
        count = (
            self.session
            .query(Article)
            .filter(Article.is_deleted.is_(False))
            .update(
                {
                    Article.is_deleted: True, 
                    Article.deleted_at: now
                }, 
                synchronize_session=False
            )
        )
        self.session.flush()
        return count

    def update(
            self, 
            *,
            article: Article,  
            new_title: str | None = None, 
            new_normalized_title: str | None = None,
            new_url: str | None = None
        ) -> None:
        if new_title is not None:
            article.title = new_title
            article.normalized_title = new_normalized_title
        if new_url is not None:
            article.url = new_url
        self.session.flush()