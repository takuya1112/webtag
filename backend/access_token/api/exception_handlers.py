from fastapi import FastAPI, status

from ..domain.exceptions import (
    AccessTokenDomainError,
    ExpiredAccessTokenError,
    InvalidAccessTokenError,
)
from ..infrastructure.exceptions import (
    AccessTokenInfrastructureError,
)
from .handlers import create_domain_handler

INFRASTRUCTURE_EXCEPTION_HANDLERS: dict[
    type[AccessTokenInfrastructureError],
    tuple[int, str],
] = {}

DOMAIN_EXCEPTION_HANDLERS: dict[
    type[AccessTokenDomainError],
    tuple[int, str],
] = {
    ExpiredAccessTokenError: (
        status.HTTP_401_UNAUTHORIZED,
        "EXPIRED_ACCESS_TOKEN",
    ),
    InvalidAccessTokenError: (
        status.HTTP_401_UNAUTHORIZED,
        "INVALID_ACCESS_TOKEN",
    ),
}


def register_access_token_exception_handlers(app: FastAPI) -> None:
    for exc_type, (
        status_code,
        error_code,
    ) in DOMAIN_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_domain_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )
