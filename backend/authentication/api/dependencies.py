from typing import Annotated

from access_token.api.dependencies import JwtServiceDep
from core import get_logger
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from refresh_token.api.dependencies import CreateRefreshTokenDep, HMACHasherDep
from refresh_token.infrastructure.repository import (
    SQLAlchemyRefreshTokenRepository,
)
from shared.api.dependencies import ClockDep, UOWDep
from user.api.dependencies import Argon2HasherDep, CreateUserDep
from user.domain.entity import UserEntity
from user.infrastructure.repository import SQLAlchemyUserRepository

from ..application import GetCurrentUser, Login, Logout, Signup

logger = get_logger(__name__)


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


def get_login(
    uow: UOWDep,
    create_refresh_token: CreateRefreshTokenDep,
    jwt_service: JwtServiceDep,
    password_hasher: Argon2HasherDep,
):
    return Login(
        uow=uow,
        repository=SQLAlchemyUserRepository,
        create_refresh_token=create_refresh_token,
        jwt_service=jwt_service,
        password_hasher=password_hasher,
    )


LoginDep = Annotated[
    Login,
    Depends(get_login),
]


def get_logout(
    uow: UOWDep,
    token_hasher: HMACHasherDep,
    clock: ClockDep,
):
    return Logout(
        uow=uow,
        repository=SQLAlchemyRefreshTokenRepository,
        token_hasher=token_hasher,
        clock=clock,
    )


LogoutDep = Annotated[
    Logout,
    Depends(get_logout),
]


def get_get_current_user(
    uow: UOWDep,
    jwt_service: JwtServiceDep,
) -> GetCurrentUser:
    return GetCurrentUser(
        uow=uow,
        jwt_service=jwt_service,
    )


GetCurrentUserDep = Annotated[
    GetCurrentUser,
    Depends(get_get_current_user),
]

security = HTTPBearer()
CredentialsDep = Annotated[
    HTTPAuthorizationCredentials,
    Depends(security),
]


def get_current_user(
    credentials: CredentialsDep,
    usecase: GetCurrentUserDep,
) -> UserEntity:
    token = credentials.credentials
    return usecase.execute(token)


CurrentUserDep = Annotated[
    UserEntity,
    Depends(get_current_user),
]
