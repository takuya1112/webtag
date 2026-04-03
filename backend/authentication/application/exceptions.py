from typing import Any


class AuthenticationApplicationError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class InvalidCredentialsError(AuthenticationApplicationError):
    pass


class InvalidRefreshTokenError(AuthenticationApplicationError):
    pass


class UserUnauthorizedError(AuthenticationApplicationError):
    pass
