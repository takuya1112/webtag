from pydantic import BaseModel, ConfigDict, HttpUrl, field_validator
from enum import Enum

class ArticleCreate(BaseModel):
    title: str
    url: HttpUrl

    @field_validator("title")
    @classmethod
    def validate_title(cls, value :str) -> str:
        if not value.strip():
            raise ValueError("title must be filled")
        return value.strip()

class ArticleUpdate(BaseModel):
    title: str | None = None
    url: HttpUrl | None = None

class ArticleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    url: str

class ArticleSort(str, Enum):
    CREATED_DESC = "-created_at"
    CREATED_ASC = "created_at"
    UPDATED_DESC = "-updated_at"
    UPDATED_ASC = "updated_at"
    TITLE_DESC = "-title"
    TITLE_ASC = "title"