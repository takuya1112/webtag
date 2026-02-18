from fastapi import status
from shared.exceptions import AppException


class UserError(AppException):
    pass


class UserAlreadyInactive(UserError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_message = "User already inactive"
    error_code = "USER_ALREADY_INACTIVE"


class UserAlreadyActive(UserError):
    status_code = status.HTTP_409_CONFLICT
    default_message = "User already active"
    error_code = "USER_ALREADY_ACTIVE"


class UserNotFoundError(UserError):
    status_code = status.HTTP_404_NOT_FOUND
    default_message = "User not found"
    error_code = "USER_NOT_FOUND"
