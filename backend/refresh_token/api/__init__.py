from fastapi import APIRouter

from .dependencies import (
    CreateRefreshTokenDep,
    RefreshAccessTokenDep,
    RefreshTokenFactoryDep,
)
from .endpoints import refresh

router = APIRouter(prefix="/refresh-token", tags=["refresh-token"])
router.include_router(refresh.router)

__all__ = [
    "CreateRefreshTokenDep",
    "RefreshAccessTokenDep",
    "RefreshTokenFactoryDep",
    "router",
]
