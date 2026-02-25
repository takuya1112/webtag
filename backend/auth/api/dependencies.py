from typing import Annotated

from core import get_logger
from core.config import settings
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from refresh_token.api.dependencies import CreateRefreshTokenDep
from refresh_token.infrastructure.repository import (
    SQLAlchemyRefreshTokenRepository,
)
from shared.api.dependencies import (
    Argon2HasherDep,
    ClockDep,
    HMACHasherDep,
    UOWDep,
)
from user.api.dependencies import CreateUserDep
from user.domain.entity import UserEntity
from user.domain.value_objects import UserId
from user.infrastructure.repository import SQLAlchemyUserRepository

from ..application import Login, Logout, Signup
from ..exceptions import (
    ExpiredAccessTokenError,
    InvalidAccessTokenError,
    UserUnauthorizedError,
)
from ..infrastructure.jwt_service import PyJwtService

logger = get_logger(__name__)


def get_jwt_service(clock: ClockDep) -> PyJwtService:
    return PyJwtService(
        secret=settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
        expire_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        clock=clock,
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

security = HTTPBearer()
CredentialsDep = Annotated[
    HTTPAuthorizationCredentials,
    Depends(security),
]


def get_current_user(
    credentials: CredentialsDep,
    uow: UOWDep,
    jwt_service: JwtServiceDep,
) -> UserEntity:
    token = credentials.credentials
    try:
        user_id = UserId(jwt_service.verify(token))
    except (ExpiredAccessTokenError, InvalidAccessTokenError):
        logger.warning("Invalid token")
        raise UserUnauthorizedError()

    with uow:
        repo = uow.get_repo(SQLAlchemyUserRepository)
        user = repo.find_by_id(user_id)

    if not user:
        logger.warning("User not found: user_id=%s", user_id.value)
        raise UserUnauthorizedError()

    if not user.can_login():
        logger.warning("User can't login: user_id=%s", user_id.value)
        raise UserUnauthorizedError()
    return user


CurrentUserDep = Annotated[
    UserEntity,
    Depends(get_current_user),
]
