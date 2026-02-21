from typing import Annotated

from fastapi import Depends
from shared.api.dependencies import (
    Argon2HasherDep,
    ClockDep,
    UOWDep,
    UUIDv7GeneratorDep,
)

from ..application import CreateUser
from ..domain.factory import UserFactory
from ..infrastructure import SQLAlchemyUserRepository


def get_user_factory(
    id_generator: UUIDv7GeneratorDep,
    clock: ClockDep,
) -> UserFactory:
    return UserFactory(
        id_generator=id_generator,
        clock=clock,
    )


UserFactoryDep = Annotated[
    UserFactory,
    Depends(get_user_factory),
]


def get_create_user(
    uow: UOWDep,
    factory: UserFactoryDep,
    password_hasher: Argon2HasherDep,
) -> CreateUser:
    return CreateUser(
        uow=uow,
        repository=SQLAlchemyUserRepository,
        factory=factory,
        password_hasher=password_hasher,
    )


CreateUserDep = Annotated[
    CreateUser,
    Depends(get_create_user),
]
