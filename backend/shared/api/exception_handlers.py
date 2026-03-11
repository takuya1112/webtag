from fastapi import FastAPI, status

from ..application.exceptions import (
    SharedApplicationError,
)
from ..domain.exceptions import (
    InvalidAwareDatetimeError,
    InvalidUuidError,
    SharedDomainError,
)
from ..infrastructure.exceptions import (
    SharedInfrastructureError,
)
from .handlers import (
    create_shared_application_handler,
    create_shared_domain_handler,
    create_shared_infrastructure_handler,
)

APPLICATION_EXCEPTION_HANDLERS = dict[
    type[SharedApplicationError],
    tuple[int, str],
] = {}

INFRASTRUCTURE_EXCEPTION_HANDLERS: dict[
    type[SharedInfrastructureError],
    tuple[int, str],
] = {}

DOMAIN_EXCEPTION_HANDLERS: dict[
    type[SharedDomainError],
    tuple[int, str],
] = {
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
    ) in INFRASTRUCTURE_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_shared_infrastructure_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )

    for exc_type, (
        status_code,
        error_code,
    ) in DOMAIN_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_shared_domain_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )
