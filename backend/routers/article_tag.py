from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import ArticleTagService
from ..schemas.article_tag import ArticleTagResponse
from ..schemas.tag import TagResponse

router = APIRouter(
    prefix="/articles/{article_id}/tags",
    tags=["ArticleTag"]
)

def get_article_tag_service(
        session: Session = Depends(get_session)
        ) -> ArticleTagService:
    return ArticleTagService(session)

@router.get("/", response_model=list[TagResponse])
def get_tags(
    article_id: int,
    service: ArticleTagService = Depends(get_article_tag_service)
):
    return service.read_tags(article_id)

@router.post("/{tag_id}", response_model=ArticleTagResponse, status_code=201)
def attach(
    article_id: int,
    tag_id: int,
    service: ArticleTagService = Depends(get_article_tag_service)
):
    return service.attach(
        article_id=article_id, 
        tag_id=tag_id
    )

@router.delete("/{tag_id}", status_code=204)
def remove(
    article_id: int,
    tag_id: int,
    service: ArticleTagService = Depends(get_article_tag_service)
):
    service.remove(
        article_id=article_id, 
        tag_id=tag_id
    )