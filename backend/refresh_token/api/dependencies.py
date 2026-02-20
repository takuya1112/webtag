from typing import Annotated

from core.config import settings
from fastapi import Depends
from shared.infrastructure.clock import SystemClock
from shared.infrastructure.security import (
    HMACHasher,
    SecureTokenGenerator,
    UUIDGv7generator,
)
from shared.infrastructure.uow import SQLAlchemyUnitOfWork, get_uow_dependency

from ..application import (
    CreateRefreshToken,
    RefreshAccessToken,
)
from ..domain.factory import RefreshTokenFactory
from ..infrastructure.repository import SQLAlchemyRefreshTokenRepository


def get_token_generator() -> SecureTokenGenerator:
    return SecureTokenGenerator()


def get_token_hasher() -> HMACHasher:
    return HMACHasher()


def get_id_generator() -> UUIDGv7generator:
    return UUIDGv7generator()


def get_clock_now() -> SystemClock:
    return SystemClock()


TokenGeneratorDep = Annotated[
    SecureTokenGenerator,
    Depends(get_token_generator),
]
HasherDep = Annotated[
    HMACHasher,
    Depends(get_token_hasher),
]
IdGeneratorDep = Annotated[
    UUIDGv7generator,
    Depends(get_id_generator),
]
ClockDep = Annotated[
    SystemClock,
    Depends(get_clock_now),
]
UOWDep = Annotated[
    SQLAlchemyUnitOfWork,
    Depends(get_uow_dependency),
]


def get_refresh_token_factory(
    token_generator: TokenGeneratorDep,
    hasher: HasherDep,
    id_generator: IdGeneratorDep,
    clock: ClockDep,
):
    return RefreshTokenFactory(
        token_generator=token_generator,
        hasher=hasher,
        id_generator=id_generator,
        clock=clock,
    )


FactoryDep = Annotated[
    RefreshTokenFactory,
    Depends(get_refresh_token_factory),
]


def get_create_refresh_token(
    uow: UOWDep,
    factory: FactoryDep,
    clock: ClockDep,
):
    return CreateRefreshToken(
        uow=uow,
        repository=SQLAlchemyRefreshTokenRepository,
        factory=factory,
        clock=clock,
    )


CreateRefreshTokenDep = Annotated[
    CreateRefreshToken,
    Depends(get_create_refresh_token),
]


def get_refresh_access_token(
    uow: UOWDep,
    factory: FactoryDep,
    hasher: HasherDep,
    clock: ClockDep,
):
    return RefreshAccessToken(
        uow=uow,
        repository=SQLAlchemyRefreshTokenRepository,
        factory=factory,
        hasher=hasher,
        clock=clock,
        expire_days=settings.REFRESH_TOKEN_EXPIRE_DAYS,
    )


RefreshAccessTokenDep = Annotated[
    RefreshAccessToken,
    Depends(get_refresh_access_token),
]
