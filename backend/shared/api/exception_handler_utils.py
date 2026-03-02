from fastapi import Request
from fastapi.responses import JSONResponse


def create_exception_handler(status_code: int, error_code: str, message: str):
    async def handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        headers = None
        if status_code == 401:
            headers = {"WWW-Authenticate": "Bearer"}

        return JSONResponse(
            status_code=status_code,
            content={
                "error_code": error_code,
                "detail": message,
            },
            headers=headers,
        )

    return handler


def create_json_response(
    status_code: int,
    error_code: str,
    detail: str,
) -> JSONResponse:
    headers = None
    if status_code == 401:
        headers = {"WWW-Authenticate": "Bearer"}

    return JSONResponse(
        status_code=status_code,
        content={
            "error_code": error_code,
            "detail": detail,
        },
        headers=headers,
    )
