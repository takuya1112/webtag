from typing import Any


class RefreshTokenApplicationError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class InvalidRefreshTokenError(RefreshTokenApplicationError):
    pass


class TokenStolenError(RefreshTokenApplicationError):
    pass
