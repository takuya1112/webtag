from fastapi import FastAPI, status

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
from .handlers import (
    create_user_application_handler,
    create_user_domain_handler,
    create_user_infrastructure_handler,
)

APPLICATION_EXCEPTION_HANDLERS = {
    EmailAlreadyExistError: (
        status.HTTP_409_CONFLICT,
        "EMAIL_ALREADY_EXIST",
    ),
}

INFRASTRUCTURE_EXCEPTION_HANDLER = {
    UserNotFoundError: (
        status.HTTP_404_NOT_FOUND,
        "USER_NOT_FOUND",
    ),
}

DOMAIN_EXCEPTION_HANDLER = {
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


def register_user_exception_handlers(app: FastAPI) -> None:
    for exc_type, (
        status_code,
        error_code,
    ) in APPLICATION_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_user_application_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )

    for exc_type, (
        status_code,
        error_code,
    ) in INFRASTRUCTURE_EXCEPTION_HANDLER.items():
        app.add_exception_handler(
            exc_type,
            create_user_infrastructure_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )

    for exc_type, (status_code, error_code) in DOMAIN_EXCEPTION_HANDLER.items():
        app.add_exception_handler(
            exc_type,
            create_user_domain_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )
