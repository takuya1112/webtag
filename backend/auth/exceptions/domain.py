class AuthDomainError(Exception):
    pass


class ExpiredAccessTokenError(AuthDomainError):
    pass


class InvalidAccessTokenError(AuthDomainError):
    pass
