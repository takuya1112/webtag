from core.constants import UserConfig
from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
    model_validator,
)
from typing_extensions import Self

from .fields import ValidateNameRequired, ValidatePasswordRequired


class SignupRequest(BaseModel):
    name: ValidateNameRequired
    email: EmailStr
    password: ValidatePasswordRequired
    password_repeat: ValidatePasswordRequired

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        if len(v) > UserConfig.EMAIL_LENGTH_MAX:
            raise ValueError("Email is too long")
        return v

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("Passwords do not match")
        return self


class SignupResponse(BaseModel):
    access_token: str
    refresh_token: str
