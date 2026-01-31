from pydantic import BaseModel, ConfigDict, HttpUrl

class ArticleCreate(BaseModel):
    title: str
    url: HttpUrl

class ArticleUpdate(BaseModel):
    title: str | None = None
    url: HttpUrl | None = None

class ArticleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    url: str
