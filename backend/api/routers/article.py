from fastapi import APIRouter, Query
from ..dependencies import (
   ArticleServiceDep, CurrentUserDep,
) 
from schemas.article import (
    ArticleCreate, 
    ArticleResponse, 
    ArticleSort, 
    ArticleUpdate,
)


router = APIRouter(
    prefix="/articles",
    tags=["Article"],
)

@router.post("/", response_model=ArticleResponse, status_code=201)
def post(
    service: ArticleServiceDep,
    create_data: ArticleCreate,
    current_user: CurrentUserDep,
):
    return service.create(create_data, current_user.id)

@router.delete("/{article_id}", status_code=204)
def soft_delete(
    service: ArticleServiceDep,
    article_id: int,
):
    service.soft_delete(article_id)

@router.delete("/", status_code=204)
def soft_delete_all(
    service: ArticleServiceDep,
):
    service.soft_delete_all()

@router.get("/{article_id}", response_model=ArticleResponse)
def get(
    service: ArticleServiceDep,
    article_id: int,
):
    return service.get_article_or_raise(article_id)

@router.get("/", response_model=list[ArticleResponse])
def get_all(
    service: ArticleServiceDep,
    q: list[str] = Query(default=[]),
    sort: ArticleSort = ArticleSort.CREATED_DESC,
):  
    return service.read_all(sort=sort, keywords=q)

@router.patch("/{article_id}", response_model=ArticleResponse)
def patch(
    service: ArticleServiceDep,
    article_id: int, 
    update_data: ArticleUpdate,
):
    return service.update(
        article_id=article_id,
        update_data=update_data,
    )