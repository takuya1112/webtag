from fastapi import status


class AppException(Exception):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_message: str = "internal error"
    error_code: str = "INTERNAL_ERROR"
    default_headers: dict[str, str] | None = None

    def __init__(
        self,
        message: str | None = None,
        headers: dict[str, str] | None = None,
    ):
        self.message = message or self.default_message
        self.headers = headers or self.default_headers
        super().__init__(self.message)

    def to_dict(self) -> dict[str, str]:
        return {
            "error_code": self.error_code,
            "detail": self.message,
        }
