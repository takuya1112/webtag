from fastapi import APIRouter

from .dependencies import (
    ClockDep,
    CreateRefreshTokenDep,
    FactoryDep,
    HasherDep,
    IdGeneratorDep,
    RefreshAccessTokenDep,
    TokenGeneratorDep,
    UOWDep,
)
from .endpoints import refresh

router = APIRouter(prefix="/auth", tags=["auth"])
router.include_router(refresh.router)

__all__ = [
    "ClockDep",
    "CreateRefreshTokenDep",
    "FactoryDep",
    "HasherDep",
    "IdGeneratorDep",
    "RefreshAccessTokenDep",
    "TokenGeneratorDep",
    "UOWDep",
    "router",
]
