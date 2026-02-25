from fastapi import APIRouter

from .dependencies import CurrentUserDep, JwtServiceDep, LoginDep, SignupDep
from .endpoints import login, logout, signup

router = APIRouter(prefix="/auth", tags=["auth"])
router.include_router(signup.router)
router.include_router(logout.router)
router.include_router(login.router)

__all__ = [
    "CurrentUserDep",
    "JwtServiceDep",
    "LoginDep",
    "SignupDep",
    "router",
]
