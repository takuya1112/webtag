from fastapi import FastAPI, status

from ..application.exceptions import (
    InvalidRefreshTokenError,
    RefreshTokenApplicationError,
    TokenStolenError,
)
from ..domain.exceptions import (
    RefreshTokenAlreadyRevokedError,
    RefreshTokenAlreadyUsedError,
    RefreshTokenCreatedAtInvalidError,
    RefreshTokenDomainError,
    RefreshTokenExpiredAtInvalidError,
    RefreshTokenExpiredError,
    RefreshTokenHashEmptyError,
    RefreshTokenRevokedAtInvalidError,
    RefreshTokenUsedAtInvalidError,
)
from ..infrastructure.exceptions import (
    RefreshTokenInfrastructureError,
    RefreshTokenTokenNotFoundError,
)
from .handlers import (
    create_application_handler,
    create_domain_handler,
    create_infrastructure_handler,
)

APPLICATION_EXCEPTION_HANDLERS: dict[
    type[RefreshTokenApplicationError],
    tuple[int, str],
] = {
    InvalidRefreshTokenError: (
        status.HTTP_401_UNAUTHORIZED,
        "INVALID_REFRESH_TOKEN",
    ),
    TokenStolenError: (
        status.HTTP_401_UNAUTHORIZED,
        "TOKEN_STOLEN",
    ),
}


INFRASTRUCTURE_EXCEPTION_HANDLERS: dict[
    type[RefreshTokenInfrastructureError], tuple[int, str]
] = {
    RefreshTokenTokenNotFoundError: (
        status.HTTP_404_NOT_FOUND,
        "REFRESH_TOKEN_NOT_FOUND",
    ),
}


DOMAIN_EXCEPTION_HANDLERS: dict[
    type[RefreshTokenDomainError], tuple[int, str]
] = {
    RefreshTokenHashEmptyError: (
        status.HTTP_400_BAD_REQUEST,
        "REFRESH_TOKEN_HASH_EMPTY",
    ),
    RefreshTokenCreatedAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "REFRESH_TOKEN_CREATED_AT_INVALID",
    ),
    RefreshTokenExpiredAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "REFRESH_TOKEN_EXPIRED_AT_INVALID",
    ),
    RefreshTokenUsedAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "REFRESH_TOKEN_USED_AT_INVALID",
    ),
    RefreshTokenRevokedAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "REFRESH_TOKEN_REVOKED_AT_INVALID",
    ),
    RefreshTokenExpiredError: (
        status.HTTP_401_UNAUTHORIZED,
        "REFRESH_TOKEN_EXPIRED",
    ),
    RefreshTokenAlreadyUsedError: (
        status.HTTP_401_UNAUTHORIZED,
        "REFRESH_TOKEN_ALREADY_USED",
    ),
    RefreshTokenAlreadyRevokedError: (
        status.HTTP_401_UNAUTHORIZED,
        "REFRESH_TOKEN_ALREADY_REVOKED",
    ),
}


def register_refresh_token_exception_handlers(app: FastAPI) -> None:
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

    for exc_type, (
        status_code,
        error_code,
    ) in INFRASTRUCTURE_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_infrastructure_handler(
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
            create_domain_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )
