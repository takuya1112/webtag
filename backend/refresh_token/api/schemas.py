from pydantic import BaseModel


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    refresh_token: str
    access_token: str
