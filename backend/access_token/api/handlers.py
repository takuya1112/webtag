from core.logging import get_logger
from fastapi import Request, status
from fastapi.responses import JSONResponse

from ..domain.exceptions import AccessTokenDomainError
from ..infrastructure.exceptions import AccessTokenInfrastructureError
from .error_messages import get_access_token_error_message

logger = get_logger(__name__)


def create_access_token_infrastructure_handler(
    status_code: int,
    error_code: str,
):
    async def handler(
        request: Request,
        exc: AccessTokenInfrastructureError,
    ) -> JSONResponse:
        logger.error(
            "Access token error: %s",
            exc.__class__.__name__,
            exc_info=True,
        )
        params = exc.context
        detail = get_access_token_error_message(
            error_code,
            **params,
        )

        if status_code >= 500:
            detail = "An error occurred"

        headers = None
        if status_code == status.HTTP_401_UNAUTHORIZED:
            headers = {"WWW-Authenticate": "Bearer"}

        return JSONResponse(
            status_code=status_code,
            content={
                "error_code": error_code,
                "detail": detail,
            },
            headers=headers,
        )

    return handler


def create_access_token_domain_handler(
    status_code: int,
    error_code: str,
):
    async def handler(
        request: Request,
        exc: AccessTokenDomainError,
    ) -> JSONResponse:
        pass
