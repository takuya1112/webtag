class AccessTokenDomainError(Exception):
    pass


class ExpiredAccessTokenError(AccessTokenDomainError):
    pass


class InvalidAccessTokenError(AccessTokenDomainError):
    pass
