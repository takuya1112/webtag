from fastapi import Request
from fastapi.responses import JSONResponse

from ..application.exceptions import (
    SharedApplicationError,
)
from ..domain.exceptions import (
    SharedDomainError,
)
from ..infrastructure.exceptions import (
    SharedInfrastructureError,
)
from .exception_handler_utils import create_json_response


def create_shared_application_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: SharedApplicationError,
    ) -> JSONResponse:
        return create_json_response(
            status_code=status_code,
            error_code=error_code,
            detail=str(exc),
        )

    return handler


def create_shared_infrastructure_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: SharedDomainError,
    ) -> JSONResponse:
        return create_json_response(
            status_code=status_code,
            error_code=error_code,
            detail=str(exc),
        )

    return handler


def create_shared_domain_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: SharedInfrastructureError,
    ) -> JSONResponse:
        return create_json_response(
            status_code=status_code,
            error_code=error_code,
            detail=str(exc),
        )

    return handler
