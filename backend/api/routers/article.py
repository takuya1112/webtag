from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..db.core import get_session
from ..db.services import ArticleService
from ..schemas.article import (
    ArticleCreate, 
    ArticleResponse, 
    ArticleSort, 
    ArticleUpdate
)

router = APIRouter(
    prefix="/articles",
    tags=["Article"]
)

def get_article_service(
        session: Session = Depends(get_session)
        ) -> ArticleService:
    return ArticleService(session)

@router.post("/", response_model=ArticleResponse, status_code=201)
def post(
    create_data: ArticleCreate,
    service: ArticleService = Depends(get_article_service)
):
    return service.create(create_data)

@router.delete("/{article_id}", status_code=204)
def soft_delete(
    article_id: int,
    service: ArticleService = Depends(get_article_service)
):
    service.soft_delete(article_id)

@router.delete("/", status_code=204)
def soft_delete_all(
    service: ArticleService = Depends(get_article_service)
):
    service.soft_delete_all()

@router.get("/{article_id}", response_model=ArticleResponse)
def get(
    article_id: int,
    service: ArticleService = Depends(get_article_service)
):
    return service.get_article_or_raise(article_id)

@router.get("/", response_model=list[ArticleResponse])
def get_all(
    q: list[str] = Query(default=[]),
    sort: ArticleSort = ArticleSort.CREATED_DESC,
    service: ArticleService = Depends(get_article_service)
):  
    return service.read_all(sort=sort, keywords=q)

@router.patch("/{article_id}", response_model=ArticleResponse)
def patch(
    article_id: int, 
    update_data: ArticleUpdate,
    service: ArticleService = Depends(get_article_service)
):
    return service.update(
        article_id=article_id,
        update_data=update_data
    )