from pydantic import BaseModel, ConfigDict
from .fields import ValidNameRequired


class TagCreate(BaseModel):
    name: ValidNameRequired

class TagUpdate(BaseModel):
    name: ValidNameRequired

class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str