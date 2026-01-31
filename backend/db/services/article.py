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

    def create(self, article: ArticleCreate) -> Article:
        new_article = Article(
            title=article.title, 
            normalized_title=article.title.lower(), 
            url=str(article.url)
        )
        self.repo.add(new_article)
        return new_article

    def soft_delete(self, article_id: int) -> None:
        article = self.get_article_or_raise(article_id)
        self.repo.soft_delete(article)

    def soft_delete_all(self) -> None:
        self.repo.soft_delete_all()

    def read(self, article_id: int) -> Article:
        return self.get_article_or_raise(article_id)

    def read_all(self, sort: ArticleSort) -> list[Article]:        
        return self.repo.get_all(sort)
    
    def update(self, article_id: int, article: ArticleUpdate) -> Article:
        ###TODO Put を patch　にしたい 
        title = article.title
        new_normalized_title = title.strip().lower()
        url = article.url

        article = self.get_article_or_raise(article_id)
        self.repo.update(
            article=article, 
            title=title,
            normalized_title=new_normalized_title,
            url=url
        )
        return article