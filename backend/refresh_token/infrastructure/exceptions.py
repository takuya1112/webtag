from typing import Any


class RefreshTokenInfrastructureError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }


class RefreshTokenTokenNotFoundError(RefreshTokenInfrastructureError):
    pass
