from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, model_validator
from uuid import UUID
from .fields import ValidateName, ValidateEmail, ValidatePassword

class UserCreate(BaseModel):
    name: ValidateName
    email: ValidateEmail
    password: ValidatePassword
    password_repeat: ValidatePassword

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("Passwords do not match")
        return self
    
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    public_id: UUID
    name: str
    email: str