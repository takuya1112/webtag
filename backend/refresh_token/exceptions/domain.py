class RefreshTokenDomainError(Exception):
    pass


class ExpiredTokenError(RefreshTokenDomainError):
    pass


class TokenAlreadyUsed(RefreshTokenDomainError):
    pass


class TokenAlreadyRevoked(RefreshTokenDomainError):
    pass
