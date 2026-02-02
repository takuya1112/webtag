from sqlalchemy.orm import Session
from ..models import Article
from ..repositories import ArticleRepository
from fastapi import HTTPException, status
from ...schemas.article import ArticleCreate, ArticleUpdate, ArticleSort


class ArticleService:
    def __init__(self, session: Session):
        self.repo = ArticleRepository(session)

    def get_article_or_raise(self, article_id: int) -> Article:
        article = self.repo.get(article_id)
        if not article or article.is_deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Article not found"
            )
        return article

    def create(self, create_data: ArticleCreate) -> Article:
        article = Article(
            title=create_data.title, 
            url=str(create_data.url)
        )
        self.repo.add(article)
        return article

    def soft_delete(self, article_id: int) -> None:
        article = self.get_article_or_raise(article_id)
        self.repo.soft_delete(article)

    def soft_delete_all(self) -> None:
        self.repo.soft_delete_all()

    def read_all(self, sort: ArticleSort) -> list[Article]:        
        return self.repo.get_all(sort)
    
    def update(self, *, article_id: int, update_data: ArticleUpdate) -> Article:
        article = self.get_article_or_raise(article_id)
        self.repo.update(
            article=article, 
            update_data=update_data
        )
        return article