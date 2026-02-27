from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from ..application.exceptions import (
    EmailAlreadyExistError,
)
from ..domain.exceptions import (
    InvalidEmailError,
    InvalidHashedPasswordError,
    InvalidUserNameError,
    UserAlreadyActive,
    UserAlreadyInactive,
)
from ..infrastructure.exceptions import (
    UserNotFoundError,
)

EXCEPTION_HANDLERS = {
    # Application
    EmailAlreadyExistError: (
        status.HTTP_409_CONFLICT,
        "EMAIL_ALREADY_EXIST",
    ),
    # Infrastructure
    UserNotFoundError: (
        status.HTTP_404_NOT_FOUND,
        "USER_NOT_FOUND",
    ),
    # Domain
    InvalidEmailError: (
        status.HTTP_400_BAD_REQUEST,
        "INVALID_EMAIL",
    ),
    InvalidHashedPasswordError: (
        status.HTTP_400_BAD_REQUEST,
        "INVALID_HASHED_PASSWORD",
    ),
    InvalidUserNameError: (
        status.HTTP_400_BAD_REQUEST,
        "INVALID_USER_NAME",
    ),
    UserAlreadyActive: (
        status.HTTP_400_BAD_REQUEST,
        "USER_ALREADY_ACTIVE",
    ),
    UserAlreadyInactive: (
        status.HTTP_400_BAD_REQUEST,
        "USER_ALREADY_INACTIVE",
    ),
}


def _create_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={
                "error_code": error_code,
                "detail": str(exc),
            },
        )

    return handler


# Registration
def register_user_exception_handlers(app: FastAPI) -> None:
    for exc_type, (status_code, error_code) in EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            _create_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )
