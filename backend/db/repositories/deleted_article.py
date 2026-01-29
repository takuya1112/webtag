from sqlalchemy import func, text
from sqlalchemy.orm import Session
from ..models import Article


class DeletedArticleRepository:
    DELETE_INTERVAL = 30

    def __init__(self, session: Session):
        self.session = session

    def delete_outdated_articles(self) -> int:
        count = self.session.query(Article).filter(
            Article.is_deleted.is_(True),
            Article.deleted_at < func.now() - text(f"INTERVAL '{self.DELETE_INTERVAL} days'")
        ).delete(synchronize_session=False)
        self.session.flush()
        return count

    def get_deleted_article_or_raise(self, article_id: int) -> Article:
        deleted_article = self.session.get(Article, article_id)
        if not deleted_article:
            raise ValueError(f"Article with id {article_id} not found")
        
        if not deleted_article.is_deleted:
            raise ValueError(f"Article with id {article_id} is not deleted")

        return deleted_article

    def get_all(self) -> list[Article]:
        deleted_articles = self.session.query(Article).filter(Article.is_deleted.is_(True)).all()
        return deleted_articles
    
    def hard_delete(self, article: Article) -> None:
        self.session.delete(article)
        self.session.flush()

    def hard_delete_all(self) -> int:
        count = self.session.query(Article).filter(Article.is_deleted.is_(True)).delete()
        self.session.flush()
        return count
    
    def restore(self, article: Article) -> None:
        article.is_deleted = False
        article.deleted_at = None
        self.session.flush()

    def restore_all(self) -> int:
        count = (
            self.session
            .query(Article)
            .filter(Article.is_deleted.is_(True))
            .update(
                {
                    Article.is_deleted: False, 
                    Article.deleted_at: None
                }, 
                synchronize_session=False
            )
        )
        self.session.flush()
        return count