from sqlalchemy import func, desc, asc, or_
from sqlalchemy.orm import Session
from ..models import Article, Tag
from ...schemas.article import ArticleSort, ArticleUpdate


class ArticleRepository:
    SORT_CONFIG = {
        ArticleSort.CREATED_ASC: asc(Article.created_at),
        ArticleSort.CREATED_DESC: desc(Article.created_at),
        ArticleSort.UPDATED_ASC: asc(Article.updated_at),
        ArticleSort.UPDATED_DESC: desc(Article.updated_at),
        ArticleSort.TITLE_ASC: asc(func.lower(Article.title)),
        ArticleSort.TITLE_DESC: desc(func.lower(Article.title)),
    }

    def __init__(self, session: Session):
        self.session = session

    def get(self, article_id: int) -> Article | None:
        return self.session.get(Article, article_id)
    
    def get_all(self, sort: ArticleSort) -> list[Article]:
        order_by = self.SORT_CONFIG[sort]
        return (
            self.session.query(Article)
            .filter(Article.is_deleted.is_(False))
            .order_by(order_by)
            .all()
        )
    
    def search(self, sort: ArticleSort, keywords: list[str]) -> list[Article]:
        order_by = self.SORT_CONFIG[sort]
        articles = (
            self.session.query(Article)
            .select_from(Article)
            .outerjoin(Article.tags)
            .filter(
                or_(
                    func.lower(Tag.name).in_(keywords),
                    *[func.lower(Article.title).like(f"%{keyword}%") for keyword in keywords]
                )
            )
            .order_by(order_by)
            .all()
        )

        seen = set()
        unique_articles = []
        for article in articles:
            if article.id not in seen:
                seen.add(article.id)
                unique_articles.append(article)

        return unique_articles

    
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

    def update(self, *, article: Article, update_data: ArticleUpdate) -> None:
        if "title" in update_data.model_fields_set:
            article.title = update_data.title
        if "url" in update_data.model_fields_set:
            article.url = str(update_data.url)
        self.session.flush()