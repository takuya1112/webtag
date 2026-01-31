from pydantic import BaseModel, ConfigDict

class ArticleTagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    article_id: int
    tag_id: int