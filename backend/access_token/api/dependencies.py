from typing import Annotated

from core.config import settings
from fastapi import Depends
from shared.api.dependencies import (
    ClockDep,
)

from ..infrastructure.jwt_service import PyJwtService


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
