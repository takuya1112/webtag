from fastapi import APIRouter

from .dependencies import CreateUserDep, JwtServiceDep
from .endpoints import signup

router = APIRouter(prefix="/auth", tags=["auth"])
router.include_router(signup.router)

__all__ = [
    "CreateUserDep",
    "JwtServiceDep",
    "router",
]
