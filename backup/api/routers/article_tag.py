from fastapi import APIRouter
from ..dependencies import ArticleTagServiceDep
from schemas.article_tag import ArticleTagResponse
from schemas.tag import TagResponse


router = APIRouter(
    prefix="/articles/{article_id}/tags",
    tags=["ArticleTag"],
)

@router.get("/", response_model=list[TagResponse])
def get_tags(
    service: ArticleTagServiceDep,
    article_id: int,
):
    return service.read_tags(article_id)

@router.post("/{tag_id}", response_model=ArticleTagResponse, status_code=201)
def attach(
    service: ArticleTagServiceDep,
    article_id: int,
    tag_id: int,
):
    return service.attach(
        article_id=article_id, 
        tag_id=tag_id,
    )

@router.delete("/{tag_id}", status_code=204)
def remove(
    service: ArticleTagServiceDep,
    article_id: int,
    tag_id: int,
):
    service.remove(
        article_id=article_id, 
        tag_id=tag_id,
    )