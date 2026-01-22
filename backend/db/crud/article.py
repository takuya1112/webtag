from sqlalchemy import func
from sqlalchemy.orm import Session
from ..models import Article


def _get_article_or_raise(session: Session, article_id: int) -> Article:
    article = session.get(Article, article_id)
    if not article or article.is_deleted:
        raise ValueError(f"Article with id {article_id} not found")
    return article


def create(session: Session, title: str, url: str) -> Article:
    new_article = Article(title=title, url=url)
    session.add(new_article)
    return new_article


def delete(session: Session, article_id: int) -> Article:
    article = _get_article_or_raise(session, article_id)
    article.is_deleted = True
    article.deleted_at = func.now()
    return article


def delete_all(session: Session) -> int:
    now = func.now()
    count = session.query(Article).filter(Article.is_deleted == False).update(
        {Article.is_deleted: True, Article.deleted_at: now}, synchronize_session=False
    )
    return count


def read_or(session: Session, keywords: list[str]) -> list[Article]:
    pass

def read_and(session: Session, keywords: list[str]) -> list[Article]:
    pass


def read_all(session: Session) -> list[Article]:
    articles = session.query(Article).filter(Article.is_deleted == False).all()
    return articles


def rename(session: Session, article_id: int, new_title: str) -> Article:
    article = _get_article_or_raise(session, article_id)
    article.title = new_title
    return article


def edit_url(session: Session, article_id: int, new_url: str) -> Article:
    article = _get_article_or_raise(session, article_id)
    article.url = new_url
    return article