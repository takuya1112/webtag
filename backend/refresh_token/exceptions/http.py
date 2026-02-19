from fastapi import status
from shared.exceptions import AppException


class RefreshTokenError(AppException):
    pass


class TokenNotFoundError(RefreshTokenError):
    status_code = status.HTTP_404_NOT_FOUND
    default_message = "Token not found"
    error_code = "TOKEN_NOT_FOUND"


class InvalidTokenError(RefreshTokenError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = "Invalid token"
    error_code = "INVALID_TOKEN"
    default_headers = {"WWW-Authenticate": "Bearer"}


class TokenStolenError(RefreshTokenError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = "Token stolen"
    error_code = "TOKEN_STOLEN"
    default_headers = {"WWW-Authenticate": "Bearer"}
