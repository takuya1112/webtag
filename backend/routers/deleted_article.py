from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import DeletedArticleService

router = APIRouter(
    prefix="/articles/deleted",
    tags=["Article"]
)

def get_deleted_article_service(
        session: Session = Depends(get_session)
        ) -> DeletedArticleService:
    return DeletedArticleService(session)

class DeletedArticleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    url: str

class DeleteAllResponse(BaseModel):
    deleted_count: int

class RestoreAllResponse(BaseModel):
    restored_count: int

@router.get("/{article_id}", response_model=DeletedArticleResponse)
def read(
    article_id: int,
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    return service.read(article_id)

@router.get("/", response_model=list[DeletedArticleResponse])
def read_all(
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    return service.read_all()

@router.delete("/{article_id}", response_model=DeletedArticleResponse)
def hard_delete(
    article_id: int,
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    return service.hard_delete(article_id)

@router.delete("/", response_model=DeleteAllResponse)
def hard_delete_all(
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    deleted_count = service.hard_delete_all()
    return {"deleted_count": deleted_count}

@router.patch("/{article_id}", response_model=DeletedArticleResponse)
def restore(
    article_id: int,
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    return service.restore(article_id)

@router.patch("/", response_model=RestoreAllResponse)
def restore_all(
    service: DeletedArticleService = Depends(get_deleted_article_service)
):
    restored_count = service.restore_all()
    return {"restored_count": restored_count}