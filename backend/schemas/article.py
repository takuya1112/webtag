from typing import Annotated
from pydantic import BaseModel, ConfigDict, HttpUrl, AfterValidator, model_validator
from enum import Enum

def validate_title_required(title: str) -> str:
    if not title.strip():
        raise ValueError("title must be filled")
    if len(title) > 300:
        raise ValueError("title within 300 chars")
    return title.strip()

def validate_title_optional(title: str | None) -> str | None:
    if title is None:
        return None
    else:
        return validate_title_required(title)

ValidateTitleRequired = Annotated[str, AfterValidator(validate_title_required)]
ValidateTitleOptional = Annotated[str | None, AfterValidator(validate_title_optional)]

class ArticleCreate(BaseModel):
    title: ValidateTitleRequired
    url: HttpUrl

class ArticleUpdate(BaseModel):
    title: ValidateTitleOptional = None
    url: HttpUrl | None = None

    @model_validator(mode="after")
    def validate_article_update(self):
        if self.title is None and self.url is None:
            raise ValueError("title or url must be filled")
        return self

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

class RestoreAllResponse(BaseModel):
    restored_count: int