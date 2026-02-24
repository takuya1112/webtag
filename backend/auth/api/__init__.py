from fastapi import APIRouter

from .dependencies import JwtServiceDep, LoginDep, SignupDep
from .endpoints import login, signup

router = APIRouter(prefix="/auth", tags=["auth"])
router.include_router(signup.router)
router.include_router(login.router)

__all__ = [
    "JwtServiceDep",
    "LoginDep",
    "SignupDep",
    "router",
]
