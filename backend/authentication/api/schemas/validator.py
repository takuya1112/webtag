from pydantic import (
    BaseModel,
    EmailStr,
    model_validator,
)
from typing_extensions import Self

from .fields import ValidateNameRequired, ValidatePasswordRequired


class SignupRequest(BaseModel):
    name: ValidateNameRequired
    email: EmailStr
    password: ValidatePasswordRequired
    password_repeat: ValidatePasswordRequired

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("Passwords do not match")
        return self


class SignupResponse(BaseModel):
    access_token: str
    refresh_token: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: ValidatePasswordRequired


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str


class LogoutRequest(BaseModel):
    refresh_token: str
