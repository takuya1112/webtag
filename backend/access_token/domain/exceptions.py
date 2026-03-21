from typing import Any


class AccessTokenDomainError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class ExpiredAccessTokenError(AccessTokenDomainError):
    pass


class InvalidAccessTokenError(AccessTokenDomainError):
    pass
