from sqlalchemy.orm import Session
from ..models import Article
from ..repositories import DeletedArticleRepository
from fastapi import HTTPException, status


class DeletedArticleService:
    def __init__(self, session: Session):
        self.repo = DeletedArticleRepository(session)

    def get_deleted_article_or_raise(self, article_id: int) -> Article:
        deleted_article = self.repo.session.get(Article, article_id)
        if not deleted_article:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Article not found"
            )
        
        if not deleted_article.is_deleted:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Article is not deleted"
            )
        return deleted_article
    
    def hard_delete(self, article_id: int) -> None:
        article = self.get_deleted_article_or_raise(article_id)
        self.repo.hard_delete(article)

    def hard_delete_all(self) -> None:
        self.repo.hard_delete_all()

    def read(self, article_id: int) -> Article:
        self.repo.delete_outdated_articles()
        deleted_article = self.get_deleted_article_or_raise(article_id)
        return deleted_article

    def read_all(self) -> list[Article]:
        self.repo.delete_outdated_articles()
        deleted_articles = self.repo.get_all()
        return deleted_articles

    def restore(self, article_id: int) -> Article:
        article = self.get_deleted_article_or_raise(article_id)
        self.repo.restore(article)
        return article

    def restore_all(self) -> int:
        count = self.repo.restore_all()
        return count