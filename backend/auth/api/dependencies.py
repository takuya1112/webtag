from typing import Annotated

from core.config import settings
from fastapi import Depends
from refresh_token.api.dependencies import CreateRefreshTokenDep
from shared.api.dependencies import ClockDep
from user.api.dependencies import CreateUserDep

from ..application import Signup
from ..infrastructure.jwt_service import PyJwtService


def get_jwt_service() -> PyJwtService:
    return PyJwtService(
        secret=settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
        expire_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        clock=ClockDep,
    )


JwtServiceDep = Annotated[
    PyJwtService,
    Depends(get_jwt_service),
]


def get_signup(
    create_user: CreateUserDep,
    create_refresh_token: CreateRefreshTokenDep,
    jwt_service: JwtServiceDep,
):
    return Signup(
        create_user=create_user,
        create_refresh_token=create_refresh_token,
        jwt_service=jwt_service,
    )


SignupDep = Annotated[
    Signup,
    Depends(get_signup),
]
