from sqlalchemy.orm import Session
from ..models import Article
from ..repositories import ArticleRepository


class ArticleService:
    def __init__(self, session: Session):
        self.repo = ArticleRepository(session)

    def create(self, title: str, url: str) -> Article:
        new_article = Article(title=title, url=url)
        self.repo.add(new_article)
        return new_article

    def delete(self, article_id: int) -> Article:
        article = self.repo.get_article_or_raise(article_id)
        self.repo.delete(article)
        return article

    def delete_all(self) -> int:
        count = self.repo.delete_all()
        return count

    def read(self, article_id: int) -> Article:
        article = self.repo.get_article_or_raise(article_id)
        return article

    def read_all(self) -> list[Article]:
        articles = self.repo.get_all()
        return articles

    def update(
            self, 
            article_id: int, 
            *, 
            new_title: str | None = None, 
            new_url: str | None = None
        ) -> Article:
        article = self.repo.get_article_or_raise(article_id)
        self.repo.update(article=article, new_title=new_title, new_url=new_url)
        return article