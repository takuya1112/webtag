from fastapi import status
from shared.exceptions import AppException


class AuthError(AppException):
    pass


class InvalidCredentialsError(AuthError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = "Invalid credentials"
    error_code = "INVALID_CREDENTIALS"
    default_headers = {"WWW-Authenticate": "Bearer"}
