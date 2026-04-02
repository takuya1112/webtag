from typing import Any


class RefreshTokenInfrastructureError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class RefreshTokenTokenNotFoundError(RefreshTokenInfrastructureError):
    pass
