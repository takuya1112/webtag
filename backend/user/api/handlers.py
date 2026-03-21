from core.logging import get_logger
from fastapi import Request, status
from fastapi.responses import JSONResponse

from ..application.exceptions import (
    UserApplicationError,
)
from ..domain.exceptions import (
    UserDomainError,
)
from ..infrastructure.exceptions import (
    UserInfrastructureError,
)
from .error_messages import get_error_message

logger = get_logger(__name__)


def create_application_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: UserApplicationError,
    ) -> JSONResponse:
        logger.debug(
            "User application error: %s",
            exc.__class__.__name__,
        )
        params = exc.context
        detail = get_error_message(
            error_code,
            **params,
        )

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


def create_infrastructure_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: UserInfrastructureError,
    ) -> JSONResponse:
        logger.error(
            "User infrastructure error: %s",
            exc.__class__.__name__,
            exc_info=True,
        )
        params = exc.context
        detail = get_error_message(
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


def create_domain_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: UserDomainError,
    ) -> JSONResponse:
        logger.debug(
            "User domain error: %s",
            exc.__class__.__name__,
        )
        params = exc.context
        detail = get_error_message(
            error_code,
            **params,
        )

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
