from sqlalchemy.orm import Session
from ..models import Article
from ..repositories import DeletedArticleRepository


class DeletedArticleService:
    def __init__(self, session: Session):
        self.repo = DeletedArticleRepository(session)

    def read(self, article_id: int) -> Article:
        deleted_article = self.repo.get_deleted_article_or_raise(article_id)
        return deleted_article

    def read_all(self) -> list[Article]:
        self.repo.delete_outdated_articles()
        deleted_articles = self.repo.get_all()
        return deleted_articles

    def hard_delete(self, article_id: int) -> Article:
        article = self.repo.get_deleted_article_or_raise(article_id)
        self.repo.hard_delete(article)
        return article

    def hard_delete_all(self) -> int:
        count = self.repo.hard_delete_all()
        return count

    def restore(self, article_id: int) -> Article:
        article = self.repo.get_deleted_article_or_raise(article_id)
        self.repo.restore(article)
        return article

    def restore_all(self) -> int:
        count = self.repo.restore_all()
        return count