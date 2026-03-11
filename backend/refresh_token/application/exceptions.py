class RefreshTokenApplicationError(Exception):
    pass


class TokenNotFoundError(RefreshTokenApplicationError):
    pass


class InvalidTokenError(RefreshTokenApplicationError):
    pass


class TokenStolenError(RefreshTokenApplicationError):
    pass
