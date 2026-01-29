from sqlalchemy.orm import Session
from ..models import ArticleTag
from ..repositories import ArticleTagRepository


class ArticleTagService:
    def __init__(self, session: Session):
        self.repo = ArticleTagRepository(session)

    def get_article_tag_or_raise(self, article_id: int, tag_id: int) -> ArticleTag:
        article_tag = self.repo.get(article_id, tag_id)
        if not article_tag:
            raise ValueError(f"Tag with id {tag_id} is not tagging Article with id {article_id}")
        return article_tag

    def attach(self, *, article_id: int, tag_id: int) -> ArticleTag:
        exsiting = self.repo.get(article_id=article_id, tag_id=tag_id)
        if exsiting:
            return exsiting

        new_article_tag = ArticleTag(article_id=article_id, tag_id=tag_id)
        self.repo.add(new_article_tag)
        return new_article_tag

    def remove(self, *, article_id: int, tag_id: int) -> ArticleTag:
        article_tag = self.get_article_tag_or_raise(article_id, tag_id)
        self.repo.delete(article_tag)
        return article_tag