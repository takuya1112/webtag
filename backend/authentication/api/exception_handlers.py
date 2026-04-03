from fastapi import FastAPI, status

from ..application.exceptions import (
    AuthenticationApplicationError,
    InvalidCredentialsError,
    InvalidRefreshTokenError,
    UserUnauthorizedError,
)
from .handlers import create_application_handler

APPLICATION_EXCEPTION_HANDLERS: dict[
    type[AuthenticationApplicationError],
    tuple[int, str],
] = {
    InvalidCredentialsError: (
        status.HTTP_401_UNAUTHORIZED,
        "INVALID_CREDENTIALS",
    ),
    InvalidRefreshTokenError: (
        status.HTTP_401_UNAUTHORIZED,
        "INVALID_REFRESH_TOKEN",
    ),
    UserUnauthorizedError: (
        status.HTTP_401_UNAUTHORIZED,
        "USER_UNAUTHORIZE",
    ),
}


def register_auth_exception_handlers(app: FastAPI) -> None:
    for exc_type, (
        status_code,
        error_code,
    ) in APPLICATION_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_application_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )
