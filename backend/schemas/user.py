from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, model_validator

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    password_repeat: str

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("Passwords do not match")
        return self
    