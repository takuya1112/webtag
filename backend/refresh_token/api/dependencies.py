from typing import Annotated

from core.security import HMACHasher, SecureTokenGenerator
from fastapi import Depends
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


GeneratorDep = Annotated[SecureTokenGenerator, Depends(get_token_generator)]
HasherDep = Annotated[HMACHasher, Depends(get_token_hasher)]
UOWDep = Annotated[UnitOfWork, Depends(get_uow_dependency)]


def get_refresh_token_factory(generator: GeneratorDep, hasher: HasherDep):
    return RefreshTokenFactory(generator=generator, hasher=hasher)


FactoryDep = Annotated[RefreshTokenFactory, Depends(get_refresh_token_factory)]


def get_create_refresh_token(uow: UOWDep, factory: FactoryDep):
    repository = uow.get_repo(SQLAlchemyRefreshTokenRepository)
    return CreateRefreshToken(repository=repository, factory=factory)


def get_validate_refresh_token(uow: UOWDep, hasher: HasherDep):
    repository = uow.get_repo(SQLAlchemyRefreshTokenRepository)
    return ValidateRefreshToken(repository=repository, hasher=hasher)


def get_refresh_access_token(
    uow: UOWDep, factory: FactoryDep, hasher: HasherDep
):
    repository = uow.get_repo(SQLAlchemyRefreshTokenRepository)
    return RefreshAccessToken(
        repository=repository,
        factory=factory,
        hasher=hasher,
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
