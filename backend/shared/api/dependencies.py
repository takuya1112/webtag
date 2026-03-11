from typing import Annotated

from fastapi import Depends

from ..infrastructure.clock import SystemClock
from ..infrastructure.id_generator import UUIDv7generator
from ..infrastructure.uow import SQLAlchemyUnitOfWork, get_uow_dependency

UOWDep = Annotated[
    SQLAlchemyUnitOfWork,
    Depends(get_uow_dependency),
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
