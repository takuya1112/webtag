from typing import Any


class RefreshTokenDomainError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class RefreshTokenIdInvalidError(RefreshTokenDomainError):
    pass


class RefreshTokenHashEmptyError(RefreshTokenDomainError):
    pass


class ExpiredRefreshTokenError(RefreshTokenDomainError):
    pass


class RefreshTokenAlreadyUsed(RefreshTokenDomainError):
    pass


class RefreshTokenAlreadyRevoked(RefreshTokenDomainError):
    pass
