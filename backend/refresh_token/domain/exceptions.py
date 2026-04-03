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


class RefreshTokenExpiredAtInvalidError(RefreshTokenDomainError):
    pass


class RefreshTokenUsedAtInvalidError(RefreshTokenDomainError):
    pass


class RefreshTokenRevokedAtInvalidError(RefreshTokenDomainError):
    pass


class RefreshTokenExpiredError(RefreshTokenDomainError):
    pass


class RefreshTokenAlreadyUsedError(RefreshTokenDomainError):
    pass


class RefreshTokenAlreadyRevokedError(RefreshTokenDomainError):
    pass
