from sqlalchemy import func, text
from sqlalchemy.orm import Session
from ..models import Article


def _get_article_or_raise(session: Session, article_id: int):
    article = session.get(Article, article_id)
    if not article:
        raise ValueError(f"Article with id {article_id} not found")
    
    if not article.is_deleted:
        raise ValueError(f"Article with id {article_id} is not deleted")

    return article


def read_all(session: Session) -> list[Article]:
    session.query(Article).filter(
        Article.is_deleted == True,
        Article.deleted_at < func.now() - text("INTERVAL '30 days'")
        ).delete(synchronize_session=False)
    deleted_articles = session.query(Article).filter(Article.is_deleted == True).all()
    return deleted_articles


def delete(session: Session, article_id: int) -> Article:
    article = _get_article_or_raise(session, article_id)
    session.delete(article)
    return article


def delete_all(session: Session) -> int:
    count = session.query(Article).filter(Article.is_deleted == True).delete()
    return count


def restore(session: Session, article_id: int) -> Article:
    article = _get_article_or_raise(session, article_id)
    article.is_deleted = False
    article.deleted_at = None
    return article


def restore_all(session: Session) -> int:
    count = session.query(Article).filter(Article.is_deleted == True).update(
        {Article.is_deleted: False, Article.deleted_at: None}, synchronize_session=False
    )
    return count