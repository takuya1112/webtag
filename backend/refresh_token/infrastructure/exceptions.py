class RefreshTokenInfrastructureError(Exception):
    pass


class RefreshTokenTokenNotFoundError(RefreshTokenInfrastructureError):
    pass
