from typing import Annotated

from core.config import settings
from fastapi import Depends
from shared.api.dependencies import (
    ClockDep,
    HasherDep,
    TokenGeneratorDep,
    UOWDep,
    UUIDv7GeneratorDep,
)

from ..application import (
    CreateRefreshToken,
    RefreshAccessToken,
)
from ..domain.factory import RefreshTokenFactory
from ..infrastructure.repository import SQLAlchemyRefreshTokenRepository


def get_refresh_token_factory(
    token_generator: TokenGeneratorDep,
    token_hasher: HasherDep,
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
