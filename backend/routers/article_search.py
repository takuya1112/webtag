from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from ..db.database import get_session
from ..db.services import ArticleSearchService

router = APIRouter(
    prefix="/articles/search",
    tags=["Article"]
)

def get_article_search_service(
        session: Session = Depends(get_session)
        ) -> ArticleSearchService:
    return ArticleSearchService(session)

class ArticleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    url: str

@router.get("/", response_model=list[ArticleResponse])
def search(
    q: list[str] = Query(...),
    service: ArticleSearchService = Depends(get_article_search_service)
):
    return service.search(q)