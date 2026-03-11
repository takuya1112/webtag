from fastapi import APIRouter

from .dependencies import (
    CredentialsDep,
    CurrentUserDep,
    GetCurrentUserDep,
    JwtServiceDep,
    LoginDep,
    SignupDep,
)
from .endpoints import login, logout, signup

router = APIRouter(prefix="/auth", tags=["auth"])
router.include_router(signup.router)
router.include_router(logout.router)
router.include_router(login.router)

__all__ = [
    "CredentialsDep",
    "CurrentUserDep",
    "GetCurrentUserDep",
    "JwtServiceDep",
    "LoginDep",
    "SignupDep",
    "router",
]
