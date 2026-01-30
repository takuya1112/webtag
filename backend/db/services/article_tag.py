from sqlalchemy.orm import Session
from ..models import ArticleTag
from ..repositories import ArticleRepository, TagRepository, ArticleTagRepository
from fastapi import HTTPException, status


class ArticleTagService:
    def __init__(self, session: Session):
        self.article_repo = ArticleRepository(session)
        self.tag_repo = TagRepository(session)
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
        ###TODO この３つを何か違うファイルにまとめる
        article = self.article_repo.get(article_id)
        if not article or article.is_deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Article not found"
            )
        
        tag = self.tag_repo.get(tag_id)
        if not tag:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tag not found"
            )

        existing = self.repo.get(article_id=article_id, tag_id=tag_id)
        if existing:
            return HTTPException(
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