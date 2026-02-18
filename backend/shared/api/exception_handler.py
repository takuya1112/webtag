from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from ..exceptions import AppException


async def app_exception_handler(
    request: Request,
    exc: AppException,
) -> JSONResponse:
    headers = {}
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        headers["WWW-Authenticate"] = 'Bearer error="invalid_token"'
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.to_dict(),
        headers=headers,
    )


def register_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(AppException, app_exception_handler)
