from fastapi import status
from shared.exceptions import AppException


class RefreshTokenError(AppException):
    pass


class TokenNotFoundError(RefreshTokenError):
    status_code = status.HTTP_404_NOT_FOUND
    default_message = "Token not found"
    error_code = "TOKEN_NOT_FOUND"


class InvalidTokenError(RefreshTokenError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = "Invalid token"
    error_code = "INVALID_TOKEN"


class TokenAlreadyUsed(RefreshTokenError):
    status_code = status.HTTP_409_CONFLICT
    default_message = "Token already used"
    error_code = "TOKEN_ALREADY_USED"


class TokenAlreadyRevoked(RefreshTokenError):
    status_code = status.HTTP_409_CONFLICT
    default_message = "Token already revoked"
    error_code = "TOKEN_ALREADY_REVOKED"


class ExpiredTokenError(RefreshTokenError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = "Token expired"
    error_code = "TOKEN_EXPIRED"


class TokenStolenError(RefreshTokenError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = "Token stolen"
    error_code = "TOKEN_STOLEN"
