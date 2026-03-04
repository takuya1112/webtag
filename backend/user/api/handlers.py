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


def create_user_application_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: UserApplicationError,
    ) -> JSONResponse:

        detail = get_error_message(
            error_code,
            **exc.params,
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


def create_user_infrastructure_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: UserInfrastructureError,
    ) -> JSONResponse:

        detail = get_error_message(
            error_code,
            **exc.params,
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


def create_user_domain_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: UserDomainError,
    ) -> JSONResponse:

        detail = get_error_message(
            error_code,
            **exc.params,
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
