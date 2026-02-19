from fastapi import status
from shared.exceptions import AppException


class UserError(AppException):
    pass


class UserNotFoundError(UserError):
    status_code = status.HTTP_404_NOT_FOUND
    default_message = "User not found"
    error_code = "USER_NOT_FOUND"


class EmailAlreadyExistError(UserError):
    status_code = status.HTTP_409_CONFLICT
    default_message = "Email already exist"
    error_code = "EMAIL_ALREADY_EXIST"
