from fastapi import APIRouter
from ..dependencies import DeletedArticleServiceDep
from schemas.article import ArticleResponse, RestoreAllResponse

router = APIRouter(
    prefix="/articles/deleted",
    tags=["Article"]
)

@router.post("/{article_id}/restore", response_model=ArticleResponse)
def restore(
    service: DeletedArticleServiceDep,
    article_id: int,
):
    return service.restore(article_id)

@router.post("/restore", response_model=RestoreAllResponse)
def restore_all(
    service: DeletedArticleServiceDep,
):
    restored_count = service.restore_all()
    return {"restored_count": restored_count}

@router.delete("/{article_id}", status_code=204)
def hard_delete(
    service: DeletedArticleServiceDep,
    article_id: int,
):
    service.hard_delete(article_id)

@router.delete("/", status_code=204)
def hard_delete_all(
    service: DeletedArticleServiceDep,
):
    service.hard_delete_all()

@router.get("/{article_id}", response_model=ArticleResponse)
def get(
    service: DeletedArticleServiceDep,
    article_id: int,
):
    return service.read(article_id)

@router.get("/", response_model=list[ArticleResponse])
def get_all(
    service: DeletedArticleServiceDep,
):
    return service.read_all()