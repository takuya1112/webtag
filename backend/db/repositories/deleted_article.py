from sqlalchemy import func, text
from sqlalchemy.orm import Session
from ..models import Article


class DeletedArticleRepository:
    DELETE_INTERVAL = 30

    def __init__(self, session: Session):
        self.session = session

    def delete_outdated_articles(self) -> None:
        self.session.query(Article).filter(
            Article.is_deleted.is_(True),
            Article.deleted_at < func.now() - text(f"INTERVAL '{self.DELETE_INTERVAL} days'")
        ).delete(synchronize_session=False)
        self.session.flush()
    
    def get(self, article_id: int) -> Article | None:
        return self.session.get(Article, article_id)

    def get_all(self) -> list[Article]:
        return (
            self.session.query(Article)
            .filter(Article.is_deleted.is_(True))
            .order_by(Article.deleted_at.desc())
            .all()
        ) 
    
    def hard_delete(self, article: Article) -> None:
        self.session.delete(article)

    def hard_delete_all(self) -> None:
        self.session.query(Article).filter(Article.is_deleted.is_(True)).delete()
        
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