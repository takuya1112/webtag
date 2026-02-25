from fastapi import status
from shared.exceptions import AppException


class AuthError(AppException):
    pass


class InvalidCredentialsError(AuthError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = "Invalid credentials"
    error_code = "INVALID_CREDENTIALS"
    default_headers = {"WWW-Authenticate": "Bearer"}


class UserUnauthorizedError(AuthError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = "User unauthorize"
    error_code = "USER_UNAUTHORIZE"
    default_headers = {"WWW-Authenticate": "Bearer"}
