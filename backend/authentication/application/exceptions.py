from typing import Any


class AuthenticationApplicationError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }


class InvalidCredentialsError(AuthenticationApplicationError):
    pass


class InvalidRefreshTokenError(AuthenticationApplicationError):
    pass


class UserUnauthorizedError(AuthenticationApplicationError):
    pass
