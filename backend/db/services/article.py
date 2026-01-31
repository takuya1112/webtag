from sqlalchemy.orm import Session
from ..models import Article
from ..repositories import ArticleRepository
from fastapi import HTTPException, status
from pydantic import HttpUrl
from ...schemas.article import ArticleCreate, ArticleUpdate


class ArticleService:
    def __init__(self, session: Session):
        self.repo = ArticleRepository(session)

    def normalize_url_or_raise(self, url: HttpUrl) -> str:
        if not url:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="url must be filled"
            )
        return str(url)

    def normalize_title_or_raise(self, title: str) -> str:
        if not title or not title.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="title must be filled"
            )
        return title.lower().strip()
    
    def get_article_or_raise(self, article_id: int) -> Article:
        article = self.repo.get(article_id)
        if not article or article.is_deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Article not found"
            )
        return article

    def create(self, article: ArticleCreate) -> Article:
        title = article.title
        normalized_title = self.normalize_title_or_raise(title)
        url = self.normalize_url_or_raise(article.url)

        new_article = Article(
            title=title, 
            normalized_title=normalized_title, 
            url=url
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

    def read_all(self) -> list[Article]:
        return self.repo.get_all()

    def update(self, article_id: int, article: ArticleUpdate) -> Article:
        title = article.title
        new_normalized_title = self.normalize_title_or_raise(title)
        url = self.normalize_url_or_raise(article.url)
        article = self.get_article_or_raise(article_id)
        self.repo.update(
            article=article, 
            title=title,
            normalized_title=new_normalized_title,
            url=url
        )
        return article