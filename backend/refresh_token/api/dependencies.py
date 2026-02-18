from typing import Annotated

from fastapi import Depends
from shared.infrastructure.clock import SystemClock
from shared.infrastructure.security import (
    HMACHasher,
    SecureTokenGenerator,
    UUIDGv7generator,
)
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
    UnitOfWork,
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
    repository = uow.get_repo(SQLAlchemyRefreshTokenRepository)
    return CreateRefreshToken(
        repository=repository,
        factory=factory,
        clock=clock,
    )


CreateRefreshTokenDep = Annotated[
    CreateRefreshToken,
    Depends(get_create_refresh_token),
]


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


ValidateRefreshTokenDep = Annotated[
    ValidateRefreshToken,
    Depends(get_validate_refresh_token),
]


def get_refresh_access_token(
    uow: UOWDep,
    validator: ValidateRefreshTokenDep,
    factory: FactoryDep,
    hasher: HasherDep,
    clock: ClockDep,
):
    repository = uow.get_repo(SQLAlchemyRefreshTokenRepository)
    return RefreshAccessToken(
        repository=repository,
        validator=validator,
        factory=factory,
        hasher=hasher,
        clock=clock,
    )


RefreshAccessTokenDep = Annotated[
    RefreshAccessToken,
    Depends(get_refresh_access_token),
]
