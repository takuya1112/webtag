from pydantic import BaseModel, ConfigDict, field_validator

class TagBase(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value :str) -> str:
        if not value.strip():
            raise ValueError("name must be filled")
        return value.strip()    

class TagCreate(TagBase):
    pass

class TagUpdate(TagBase):
    pass

class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str