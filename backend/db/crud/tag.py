from sqlalchemy.orm import Session
from ..models import Tag, ArticleTag


def _get_tag_or_raise(session: Session, tag_id: int) -> Tag:
    tag = session.get(Tag, tag_id)
    if not tag:
        raise ValueError(f"Tag with id {tag_id} not found")
    return tag


def create(session: Session, name: str) -> Tag:
    new_tag = Tag(name=name, name_lower=name.lower())
    session.add(new_tag)
    return new_tag


def delete(session: Session, tag_id: int) -> Tag:
    tag = _get_tag_or_raise(session, tag_id)
    session.delete(tag)
    return tag


def delete_all(session: Session) -> int:
    count = session.query(Tag).delete()
    return count


def read(session: Session, tag_id: int) -> Tag:
    tag = _get_tag_or_raise(session, tag_id)
    return tag


def read_all(session: Session) -> list[Tag]:
    tags = session.query(Tag).all()
    return tags


def update(session: Session, tag_id: int, new_name: str) -> Tag:
    tag = _get_tag_or_raise(session, tag_id)
    tag.name = new_name
    tag.name_lower = new_name.lower()
    return tag


def attach(session: Session, article_id: int, tag_id: int) -> ArticleTag:
    new_article_tag = ArticleTag(article_id=article_id, tag_id=tag_id)
    session.add(new_article_tag)
    return new_article_tag


def remove(session: Session, article_id: int, tag_id: int) -> ArticleTag:
    article_tag = session.get(ArticleTag, (article_id, tag_id))
    if not article_tag:
        raise ValueError(f"Tag with id {tag_id} is not tagging Article with id {article_id}")

    session.delete(article_tag)
    return article_tag