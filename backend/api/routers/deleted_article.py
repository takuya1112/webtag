from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.core import get_session
from ..db.services import DeletedArticleService
from ..schemas.article import ArticleResponse, RestoreAllResponse

router = APIRouter(
    prefix="/articles/deleted",
    tags=["Article"]
)

def get_deleted_article_service(
        session: Session = Depends(get_session)
        ) -> DeletedArticleService:
    return DeletedArticleService(session)

@router.post("/{article_id}/restore", response_model=ArticleResponse)
def restore(
    article_id: int,
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    return service.restore(article_id)

@router.post("/restore", response_model=RestoreAllResponse)
def restore_all(
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    restored_count = service.restore_all()
    return {"restored_count": restored_count}

@router.delete("/{article_id}", status_code=204)
def hard_delete(
    article_id: int,
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    service.hard_delete(article_id)

@router.delete("/", status_code=204)
def hard_delete_all(
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    service.hard_delete_all()

@router.get("/{article_id}", response_model=ArticleResponse)
def get(
    article_id: int,
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    return service.read(article_id)

@router.get("/", response_model=list[ArticleResponse])
def get_all(
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    return service.read_all()