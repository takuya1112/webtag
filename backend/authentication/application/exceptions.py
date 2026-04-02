from typing import Any


class AuthenticationApplicationError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class InvalidCredentialsError(AuthenticationApplicationError):
    pass


class UserUnauthorizedError(AuthenticationApplicationError):
    pass


# from fastapi import status


# class AuthError(Exception):
#     pass


# class InvalidCredentialsError(AuthError):
#     status_code = status.HTTP_401_UNAUTHORIZED
#     default_message = "Invalid credentials"
#     error_code = "INVALID_CREDENTIALS"
#     default_headers = {"WWW-Authenticate": "Bearer"}


# class UserUnauthorizedError(AuthError):
#     status_code = status.HTTP_401_UNAUTHORIZED
#     default_message = "User unauthorize"
#     error_code = "USER_UNAUTHORIZE"
#     default_headers = {"WWW-Authenticate": "Bearer"}
