from access_token.api.exception_handlers import (
    register_access_token_exception_handlers,
)
from authentication.api.exception_handlers import (
    register_auth_exception_handlers,
)
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from refresh_token.api.exception_handlers import (
    register_refresh_token_exception_handlers,
)
from user.api.exception_handlers import register_user_exception_handlers


def register_all_exception_handler(app: FastAPI) -> None:

    register_user_exception_handlers(app)
    register_access_token_exception_handlers(app)
    register_refresh_token_exception_handlers(app)
    register_auth_exception_handlers(app)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error_code": "INTERNAL_ERROR",
                "detail": "internal error",
            },
        )
