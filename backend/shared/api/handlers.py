from fastapi import Request, status
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


def create_shared_application_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: SharedApplicationError,
    ) -> JSONResponse:
        headers = None
        if status_code == status.HTTP_401_UNAUTHORIZED:
            headers = {"WWW-Authenticate": "Bearer"}

        return JSONResponse(
            status_code=status_code,
            error_code=error_code,
            headers=headers,
        )

    return handler


def create_shared_infrastructure_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: SharedDomainError,
    ) -> JSONResponse:
        headers = None
        if status_code == status.HTTP_401_UNAUTHORIZED:
            headers = {"WWW-Authenticate": "Bearer"}

        return JSONResponse(
            status_code=status_code,
            error_code=error_code,
            headers=headers,
        )

    return handler


def create_shared_domain_handler(status_code: int, error_code: str):
    async def handler(
        request: Request,
        exc: SharedInfrastructureError,
    ) -> JSONResponse:
        headers = None
        if status_code == status.HTTP_401_UNAUTHORIZED:
            headers = {"WWW-Authenticate": "Bearer"}

        return JSONResponse(
            status_code=status_code,
            error_code=error_code,
            headers=headers,
        )

    return handler
