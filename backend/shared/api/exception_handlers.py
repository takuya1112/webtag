from fastapi import FastAPI, status

from ..domain.exceptions import InvalidAwareDatetimeError, InvalidUuidError
from .handlers import (
    create_shared_application_handler,
    create_shared_domain_handler,
    create_shared_infrastructure_handler,
)

APPLICATION_EXCEPTION_HANDLERS = {}

INFRASTRUCTURE_EXCEPTION_HANDLER = {}

DOMAIN_EXCEPTION_HANDLER = {
    InvalidAwareDatetimeError: (
        status.HTTP_400_BAD_REQUEST,
        "INVALID_AWARE_DATETIME",
    ),
    InvalidUuidError: (
        status.HTTP_400_BAD_REQUEST,
        "INVALID_UUID",
    ),
}


def register_shared_exception_handlers(app: FastAPI) -> None:
    for exc_type, (
        status_code,
        error_code,
    ) in APPLICATION_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_shared_application_handler(
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
            create_shared_infrastructure_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )

    for exc_type, (status_code, error_code) in DOMAIN_EXCEPTION_HANDLER.items():
        app.add_exception_handler(
            exc_type,
            create_shared_domain_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )
