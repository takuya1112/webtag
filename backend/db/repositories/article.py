from sqlalchemy import func, desc, asc
from sqlalchemy.orm import Session
from ..models import Article
from ...schemas.article import ArticleSort


class ArticleRepository:
    def __init__(self, session: Session):
        self.session = session

    def get(self, article_id: int) -> Article | None:
        return self.session.get(Article, article_id)
    
    def get_all(self, sort: ArticleSort) -> list[Article]:
        sort_config = {
            ArticleSort.CREATED_ASC: asc(Article.created_at),
            ArticleSort.CREATED_DESC: desc(Article.created_at),
            ArticleSort.UPDATED_ASC: asc(Article.updated_at),
            ArticleSort.UPDATED_DESC: desc(Article.updated_at),
            ArticleSort.TITLE_ASC: asc(Article.normalized_title),
            ArticleSort.TITLE_DESC: desc(Article.normalized_title),
        }
        order_by = sort_config[sort]
        return (
            self.session.query(Article)
            .filter(Article.is_deleted.is_(False))
            .order_by(order_by)
            .all()
        ) 
    
    def add(self, article: Article) -> None:
        self.session.add(article)
        self.session.flush()

    def soft_delete(self, article: Article) -> None:
        article.is_deleted = True
        article.deleted_at = func.now()

    def soft_delete_all(self) -> None:
        now = func.now()
        self.session.query(Article)\
            .filter(Article.is_deleted.is_(False))\
            .update(
                {Article.is_deleted: True, Article.deleted_at: now}, 
                synchronize_session=False
            )

    def update(
            self, 
            *,
            article: Article,  
            title: str | None = None, 
            normalized_title: str | None = None,
            url: str | None = None
        ) -> None:
        article.title = title
        article.normalized_title = normalized_title
        article.url = url
        self.session.flush()