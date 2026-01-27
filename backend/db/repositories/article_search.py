from sqlalchemy import or_
from sqlalchemy.orm import Session, selectinload
from ..models import *


class ArticleSearchRepository:
    def __init__(self, session: Session):
        self.session = session

    def search_candidate(self, keywords: list[str]) -> list[Article]:
        articles = (
            self.session.query(Article)
            .select_from(Article)
            .options(
                selectinload(Article.tags)
                .selectinload(Tag.synonym)
            )
            .outerjoin(Article.tags)
            .outerjoin(Tag.synonym)
            .filter(
                or_(
                    TagSynonym.name.in_(keywords),
                    *[Article.title.ilike(f"%{keyword}%") for keyword in keywords]
                )
            )
            .distinct()
            .all()
        )
        return articles