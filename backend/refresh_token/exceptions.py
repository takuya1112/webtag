from user.domain.value_objects import UserId


class RefreshTokenError(Exception):
    pass


class TokenNotFoundError(RefreshTokenError):
    pass


class InvalidTokenError(RefreshTokenError):
    pass


class TokenAlreadyUsed(RefreshTokenError):
    def __init__(self, message: str, user_id: UserId | None = None):
        super().__init__(message)
        self.user_id = user_id


class TokenAlreadyRevoked(RefreshTokenError):
    pass


class ExpiredTokenError(RefreshTokenError):
    pass


class TokenStolenError(RefreshTokenError):
    pass
