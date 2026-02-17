from typing import Annotated

from fastapi import Depends
from shared.infrastructure.clock import SystemClock
from shared.infrastructure.security import HMACHasher, SecureTokenGenerator
from shared.infrastructure.uow import UnitOfWork, get_uow_dependency

from ..application import (
    CreateRefreshToken,
    RefreshAccessToken,
    ValidateRefreshToken,
)
from ..domain.factory import RefreshTokenFactory
from ..infrastructure.repository import SQLAlchemyRefreshTokenRepository


def get_token_generator() -> SecureTokenGenerator:
    return SecureTokenGenerator()


def get_token_hasher() -> HMACHasher:
    return HMACHasher()


def get_clock_now() -> SystemClock:
    return SystemClock()


GeneratorDep = Annotated[SecureTokenGenerator, Depends(get_token_generator)]
HasherDep = Annotated[HMACHasher, Depends(get_token_hasher)]
ClockDep = Annotated[SystemClock, Depends(get_clock_now)]
UOWDep = Annotated[UnitOfWork, Depends(get_uow_dependency)]


def get_refresh_token_factory(generator: GeneratorDep, hasher: HasherDep):
    return RefreshTokenFactory(generator=generator, hasher=hasher)


FactoryDep = Annotated[RefreshTokenFactory, Depends(get_refresh_token_factory)]


def get_create_refresh_token(
    uow: UOWDep,
    factory: FactoryDep,
    clock: ClockDep,
):
    repository = uow.get_repo(SQLAlchemyRefreshTokenRepository)
    return CreateRefreshToken(
        repository=repository,
        factory=factory,
        clock=clock,
    )


def get_validate_refresh_token(
    uow: UOWDep,
    hasher: HasherDep,
    clock: ClockDep,
):
    repository = uow.get_repo(SQLAlchemyRefreshTokenRepository)
    return ValidateRefreshToken(
        repository=repository,
        hasher=hasher,
        clock=clock,
    )


def get_refresh_access_token(
    uow: UOWDep,
    factory: FactoryDep,
    hasher: HasherDep,
    clock: ClockDep,
):
    repository = uow.get_repo(SQLAlchemyRefreshTokenRepository)
    return RefreshAccessToken(
        repository=repository,
        factory=factory,
        hasher=hasher,
        clock=clock,
    )


CreateRefreshTokenDep = Annotated[
    CreateRefreshToken,
    Depends(get_create_refresh_token),
]

ValidateRefreshTokenDep = Annotated[
    ValidateRefreshToken,
    Depends(get_validate_refresh_token),
]

RefreshAccessTokenDep = Annotated[
    RefreshAccessToken,
    Depends(get_refresh_access_token),
]
