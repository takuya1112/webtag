class TokenNotFoundError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


class TokenAlreadyRevoked(Exception):
    pass


class ExpiredTokenError(Exception):
    pass
