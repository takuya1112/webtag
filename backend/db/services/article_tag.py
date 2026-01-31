from sqlalchemy.orm import Session
from ..models import ArticleTag
from ..repositories import ArticleTagRepository
from ..services import ArticleService, TagService
from fastapi import HTTPException, status


class ArticleTagService:
    def __init__(self, session: Session):
        self.article_service = ArticleService(session)
        self.tag_service = TagService(session)
        self.repo = ArticleTagRepository(session)

    def get_article_tag_or_raise(self, article_id: int, tag_id: int) -> ArticleTag:
        article_tag = self.repo.get(article_id, tag_id)
        if not article_tag:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Tag is attached to the article"
            )
        return article_tag

    def attach(self, *, article_id: int, tag_id: int) -> ArticleTag:
        self.article_service.get_article_or_raise(article_id)
        self.tag_service.get_tag_or_raise(tag_id)
        existing = self.repo.get(article_id=article_id, tag_id=tag_id)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Tag is already attached to the article"
            )

        new_article_tag = ArticleTag(article_id=article_id, tag_id=tag_id)
        self.repo.add(new_article_tag)
        return new_article_tag

    def remove(self, *, article_id: int, tag_id: int) -> ArticleTag:
        article_tag = self.get_article_tag_or_raise(article_id, tag_id)
        self.repo.delete(article_tag)
        return article_tag