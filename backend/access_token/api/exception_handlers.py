from fastapi import FastAPI, status

from ..domain.exceptions import (
    AccessTokenDomainError,
    ExpiredAccessTokenError,
    InvalidAccessTokenError,
)
from ..infrastructure.exceptions import (
    AccessTokenInfrastructureError,
)

ACCESS_TOKEN_INFRASTRUCTURE_EXCEPTION_HANDLERS: dict[
    type[AccessTokenInfrastructureError],
    tuple[int, str],
] = {}

ACCESS_TOKEN_DOMAIN_EXCEPTION_HANDLERS: dict[
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


def register_access_token_exception_handler(app: FastAPI) -> None:
    pass
