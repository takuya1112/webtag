from pydantic import BaseModel, ConfigDict, field_validator

class TagCreate(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def validate_title(cls, value :str) -> str:
        if not value.strip():
            raise ValueError("name must be filled")
        return value.strip()

class TagUpdate(BaseModel):
    name: str

class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str