from typing import Any


class RefreshTokenApplicationError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class TokenNotFoundError(RefreshTokenApplicationError):
    pass


class InvalidTokenError(RefreshTokenApplicationError):
    pass


class TokenStolenError(RefreshTokenApplicationError):
    pass
