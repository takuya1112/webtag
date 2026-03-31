from typing import Any


class RefreshTokenDomainError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class RefreshTokenIdInvalidError(RefreshTokenDomainError):
    pass


class RefreshTokenHashEmptyError(RefreshTokenDomainError):
    pass


class RefreshTokenCreatedAtInvalidError(RefreshTokenDomainError):
    pass


class RefreshTokenExpiredAtError(RefreshTokenDomainError):
    pass


class RefreshTokenUsedAtError(RefreshTokenDomainError):
    pass


class RefreshTokenRevokedAtError(RefreshTokenDomainError):
    pass


class ExpiredRefreshTokenError(RefreshTokenDomainError):
    pass


class RefreshTokenAlreadyUsed(RefreshTokenDomainError):
    pass


class RefreshTokenAlreadyRevoked(RefreshTokenDomainError):
    pass
