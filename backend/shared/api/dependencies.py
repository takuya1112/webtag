from typing import Annotated

from fastapi import Depends

from ..infrastructure.clock import SystemClock
from ..infrastructure.security import (
    Argon2Hasher,
    HMACHasher,
    SecureTokenGenerator,
    UUIDv7generator,
)
from ..infrastructure.uow import SQLAlchemyUnitOfWork, get_uow_dependency

UOWDep = Annotated[
    SQLAlchemyUnitOfWork,
    Depends(get_uow_dependency),
]


def get_token_generator() -> SecureTokenGenerator:
    return SecureTokenGenerator()


TokenGeneratorDep = Annotated[
    SecureTokenGenerator,
    Depends(get_token_generator),
]


def get_token_hasher() -> HMACHasher:
    return HMACHasher()


HasherDep = Annotated[
    HMACHasher,
    Depends(get_token_hasher),
]


def get_uuidv7_generator() -> UUIDv7generator:
    return UUIDv7generator()


UUIDv7GeneratorDep = Annotated[
    UUIDv7generator,
    Depends(get_uuidv7_generator),
]


def get_clock_now() -> SystemClock:
    return SystemClock()


ClockDep = Annotated[
    SystemClock,
    Depends(get_clock_now),
]


def get_argon2_hasher() -> Argon2Hasher:
    return Argon2Hasher()


Argon2HasherDep = Annotated[
    Argon2Hasher,
    Depends(get_argon2_hasher),
]
