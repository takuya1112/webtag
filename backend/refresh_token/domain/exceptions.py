class RefreshTokenDomainError(Exception):
    pass


class RefreshTokenHashEmptyError(RefreshTokenDomainError):
    pass


class ExpiredRefreshTokenError(RefreshTokenDomainError):
    pass


class RefreshTokenAlreadyUsed(RefreshTokenDomainError):
    pass


class RefreshTokenAlreadyRevoked(RefreshTokenDomainError):
    pass
