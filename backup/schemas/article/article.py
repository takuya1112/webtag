from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, model_validator
from enum import Enum
from .fields import (
    ValidateTitleRequired, ValidateTitleOptional,
    ValidateUrlRequired, ValidateUrlOptional,
)

class ArticleCreate(BaseModel):
    title: ValidateTitleRequired
    url: ValidateUrlRequired

class ArticleUpdate(BaseModel):
    title: ValidateTitleOptional = None
    url: ValidateUrlOptional = None

    @model_validator(mode="after")
    def validate_article_update(self) -> Self:
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