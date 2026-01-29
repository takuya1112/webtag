from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import ArticleService

router = APIRouter(
    prefix="/articles",
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

@router.post("/", response_model=ArticleResponse)
def create(
    article: ArticleCreate,
    service: ArticleService = Depends(get_article_service)
):
    return service.create(title=article.title, url=article.url)

@router.delete("/{article_id}", response_model=ArticleResponse)
def soft_delete(
    article_id: int,
    service: ArticleService = Depends(get_article_service)
):
    return service.soft_delete(article_id)

@router.delete("/", response_model=DeleteAllResponse)
def soft_delete_all(
    service: ArticleService = Depends(get_article_service)
):
    deleted_count = service.soft_delete_all()
    return {"deleted_count": deleted_count}

@router.get("/{article_id}", response_model=ArticleResponse)
def read(
    article_id: int,
    service: ArticleService = Depends(get_article_service)
):
    return service.read(article_id)

@router.get("/", response_model=list[ArticleResponse])
def read_all(
    service: ArticleService = Depends(get_article_service)
):
    return service.read_all()

@router.patch("/{article_id}", response_model=ArticleResponse)
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