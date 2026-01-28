from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import ArticleService

article_router = APIRouter(
    prefix="/article",
    tags=["Article"]
)

def get_article_service(
        session: Session = Depends(get_session)
        ) -> ArticleService:
    return ArticleService(session)

class ArticleCreate(BaseModel):
    title: str
    url: str

class ArticleUpdate(BaseModel):
    title: str | None = None
    url: str | None = None

class ArticleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    url: str

class DeleteAllResponse(BaseModel):
    deleted_count: int

@article_router.post("/", response_model=ArticleResponse)
def create(
    article: ArticleCreate,
    service: ArticleService = Depends(get_article_service)
):
    return service.create(title=article.title, url=article.url)

@article_router.delete("/{article_id}", response_model=ArticleResponse)
def delete(
    article_id: int,
    service: ArticleService = Depends(get_article_service)
):
    return service.delete(article_id)

@article_router.delete("/", response_model=DeleteAllResponse)
def delete_all(
    service: ArticleService = Depends(get_article_service)
):
    deleted_count = service.delete_all()
    return {"deleted_count": deleted_count}

@article_router.get("/{article_id}", response_model=ArticleResponse)
def read(
    article_id: int,
    service: ArticleService = Depends(get_article_service)
):
    return service.read(article_id)

@article_router.get("/", response_model=list[ArticleResponse])
def read_all(
    service: ArticleService = Depends(get_article_service)
):
    return service.read_all()

@article_router.patch("/{article_id}", response_model=ArticleResponse)
def update(
    article_id: int, 
    article: ArticleUpdate,
    service: ArticleService = Depends(get_article_service)
):
    return service.update(
        article_id=article_id,
        new_title=article.title,
        new_url=article.url
    )