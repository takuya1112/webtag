from sqlalchemy.orm import Session
from ..models import Article
from ..repositories import ArticleRepository
from fastapi import HTTPException, status


class ArticleService:
    def __init__(self, session: Session):
        self.repo = ArticleRepository(session)

    def normalize(self, title: str) -> str:
        return title.lower().strip()
    
    def get_article_or_raise(self, article_id: int) -> Article:
        article = self.repo.get(article_id)
        if not article or article.is_deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Article not found"
            )
        return article

    def create(self, *, title: str, url: str) -> Article:
        if not title.strip() or not url.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="title and url must be filled"
            )
        normalized_title = self.normalize(title)
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
        article = self.get_article_or_raise(article_id)
        return article

    def read_all(self) -> list[Article]:
        articles = self.repo.get_all()
        return articles

    def update(
            self, 
            *,
            article_id: int,  
            new_title: str | None = None, 
            new_url: str | None = None
        ) -> Article:
        if not new_title and not new_url:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="title or url must be filled"
            )
        article = self.get_article_or_raise(article_id)
        new_normalized_title = self.normalize(new_title)
        self.repo.update(
            article=article, 
            new_title=new_title,
            new_normalized_title=new_normalized_title,
            new_url=new_url
        )
        return article