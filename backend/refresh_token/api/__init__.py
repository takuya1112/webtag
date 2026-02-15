from fastapi import APIRouter

from .dependencies import (
    CreateRefreshTokenDep,
    FactoryDep,
    GeneratorDep,
    HasherDep,
    RefreshAccessTokenDep,
    UOWDep,
    ValidateRefreshTokenDep,
)
from .endpoints import refresh

router = APIRouter(prefix="/auth", tags=["auth"])
router.include_router(refresh.router)

__all__ = [
    "CreateRefreshTokenDep",
    "FactoryDep",
    "GeneratorDep",
    "HasherDep",
    "RefreshAccessTokenDep",
    "UOWDep",
    "ValidateRefreshTokenDep",
    "router",
]
