from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import ArticleTagService

router = APIRouter(
    prefix="/articles/{article_id}/tags",
    tags=["ArticleTag"]
)

def get_article_tag_service(
        session: Session = Depends(get_session)
        ) -> ArticleTagService:
    return ArticleTagService(session)

class ArticleTagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    article_id: int
    tag_id: int

@router.post("/{tag_id}", response_model=ArticleTagResponse)
def attach(
    article_id: int,
    tag_id: int,
    service: ArticleTagService = Depends(get_article_tag_service)
):
    return service.attach(
        article_id=article_id, 
        tag_id=tag_id
    )

@router.delete("/{tag_id}", response_model=ArticleTagResponse)
def remove(
    article_id: int,
    tag_id: int,
    service: ArticleTagService = Depends(get_article_tag_service)
):
    return service.remove(
        article_id=article_id, 
        tag_id=tag_id
    )