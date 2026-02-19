from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from ..exceptions import AppException


async def app_exception_handler(
    request: Request,
    exc: AppException,
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.to_dict(),
        headers=exc.headers,
    )


def register_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(AppException, app_exception_handler)
