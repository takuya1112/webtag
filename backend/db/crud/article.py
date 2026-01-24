from sqlalchemy import func, or_
from sqlalchemy.orm import Session
from ..models import *


def _get_article_or_raise(session: Session, article_id: int) -> Article:
    article = session.get(Article, article_id)
    if not article or article.is_deleted:
        raise ValueError(f"Article with id {article_id} not found")
    return article


def create(session: Session, title: str, url: str) -> Article:
    new_article = Article(title=title, title_lower=title.lower(), url=url)
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


def read(session: Session, article_id: int) -> Article:
    article = _get_article_or_raise(session, article_id)
    return article


def read_all(session: Session) -> list[Article]:
    articles = session.query(Article).filter(Article.is_deleted == False).all()
    return articles


def rename(session: Session, article_id: int, new_title: str) -> Article:
    article = _get_article_or_raise(session, article_id)
    article.title = new_title
    article.title_lower = new_title.lower()
    return article


def edit_url(session: Session, article_id: int, new_url: str) -> Article:
    article = _get_article_or_raise(session, article_id)
    article.url = new_url
    return article


def search(session: Session, keywords: list[str]) -> list[Article]:
    if not keywords:
        return []
    
    keywords_lower = [keyword.lower() for keyword in keywords]

    articles = (
        session.query(Article)
        .select_from(Article)
        .outerjoin(ArticleTag)
        .outerjoin(Tag)
        .filter(
            or_(
                Tag.name_lower.in_(keywords_lower),
                *[Article.title.ilike(f"%{keyword}%") for keyword in keywords]
            )
        )
        .distinct()
        .all()
    )

    def caluculate_score(article: Article) -> int:
        score = 0

        article_tags = {tag.name_lower for tag in article.tags}
        tag_match = sum(1 for keyword in keywords_lower if keyword in article_tags)

        article_title = article.title_lower
        title_match = sum(1 for keyword in keywords_lower if keyword in article_title)

        if tag_match > 0 and title_match > 0:
            score += 30 + tag_match * 10 + title_match * 5
        elif tag_match > 0:
            score += 20 + tag_match * 10
        elif title_match > 0:
            score += 10 + title_match * 5
        
        return score

    articles_with_score = [(caluculate_score(article), article) for article in articles]
    articles_with_score.sort(key=lambda x: (x[0], x[1].created_at), reverse=True)
    return [article for _, article in articles_with_score]