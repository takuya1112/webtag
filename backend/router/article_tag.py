from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import ArticleTagService

article_tag_router = APIRouter(
    prefix="/article_tag",
    tags=["Article_Tag"]
)

def get_article_tag_service(
        session: Session = Depends(get_session)
        ) -> ArticleTagService:
    return ArticleTagService(session)

class ArticleTagAttach(BaseModel):
    article_id: int
    tag_id: int

class ArticleTagRemove(BaseModel):
    article_id: int
    tag_id: int

class ArticleTagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    article_id: int
    tag_id: int


@article_tag_router.post("/", response_model=ArticleTagResponse)
def attach(
    article_tag: ArticleTagAttach,
    service: ArticleTagService = Depends(get_article_tag_service)
):
    return service.attach(
        article_id=article_tag.article_id, 
        tag_id=article_tag.tag_id
    )

@article_tag_router.delete("/", response_model=ArticleTagResponse)
def remove(
    article_tag: ArticleTagRemove,
    service: ArticleTagService = Depends(get_article_tag_service)
):
    return service.remove(
        article_id=article_tag.article_id, 
        tag_id=article_tag.tag_id
    )