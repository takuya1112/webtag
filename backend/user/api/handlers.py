from fastapi import Request
from fastapi.responses import JSONResponse
from shared.api.exception_handler_utils import create_json_response

from ..application.exceptions import (
    UserApplicationError,
)
from ..domain.exceptions import (
    UserDomainError,
)
from ..infrastructure.exceptions import (
    UserInfrastructureError,
)


def create_user_application_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: UserApplicationError,
    ) -> JSONResponse:
        return create_json_response(
            status_code=status_code,
            error_code=error_code,
            detail=str(exc),
        )

    return handler


def create_user_infrastructure_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: UserInfrastructureError,
    ) -> JSONResponse:
        return create_json_response(
            status_code=status_code,
            error_code=error_code,
            detail=str(exc),
        )

    return handler


def create_user_domain_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: UserDomainError,
    ) -> JSONResponse:
        return create_json_response(
            status_code=status_code,
            error_code=error_code,
            detail=str(exc),
        )

    return handler
