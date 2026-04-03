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
from .error_messages import ERROR_MESSAGES, get_error_message
from .exception_handlers import (
    APPLICATION_EXCEPTION_HANDLERS,
    register_auth_exception_handlers,
)
from .handlers import (
    create_application_handler,
)

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
    "ERROR_MESSAGES",
    "get_error_message",
    "APPLICATION_EXCEPTION_HANDLERS",
    "register_auth_exception_handlers",
    "create_application_handler",
    "router",
]
