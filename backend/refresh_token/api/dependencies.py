from typing import Annotated

from core.config import settings
from fastapi import Depends
from shared.api.dependencies import (
    ClockDep,
    UOWDep,
    UUIDv7GeneratorDep,
)

from ..application import (
    CreateRefreshToken,
    RefreshAccessToken,
)
from ..domain.factory import RefreshTokenFactory
from ..infrastructure.refresh_token_generator import SecureRefreshTokenGenerator
from ..infrastructure.refresh_token_hasher import HMACHasher
from ..infrastructure.repository import SQLAlchemyRefreshTokenRepository


def get_token_generator() -> SecureRefreshTokenGenerator:
    return SecureRefreshTokenGenerator()


RefreshTokenGeneratorDep = Annotated[
    SecureRefreshTokenGenerator,
    Depends(get_token_generator),
]


def get_token_hasher() -> HMACHasher:
    return HMACHasher()


HMACHasherDep = Annotated[
    HMACHasher,
    Depends(get_token_hasher),
]


def get_refresh_token_factory(
    token_generator: RefreshTokenGeneratorDep,
    token_hasher: HMACHasherDep,
    id_generator: UUIDv7GeneratorDep,
    clock: ClockDep,
):
    return RefreshTokenFactory(
        token_generator=token_generator,
        token_hasher=token_hasher,
        id_generator=id_generator,
        clock=clock,
    )


RefreshTokenFactoryDep = Annotated[
    RefreshTokenFactory,
    Depends(get_refresh_token_factory),
]


def get_create_refresh_token(
    uow: UOWDep,
    factory: RefreshTokenFactoryDep,
    clock: ClockDep,
):
    return CreateRefreshToken(
        uow=uow,
        repository=SQLAlchemyRefreshTokenRepository,
        factory=factory,
        clock=clock,
        expire_days=settings.REFRESH_TOKEN_EXPIRE_DAYS,
    )


CreateRefreshTokenDep = Annotated[
    CreateRefreshToken,
    Depends(get_create_refresh_token),
]


def get_refresh_access_token(
    uow: UOWDep,
    factory: RefreshTokenFactoryDep,
    hasher: HMACHasherDep,
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
