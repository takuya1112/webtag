from fastapi import FastAPI, status

from ..application.exceptions import (
    EmailAlreadyExistError,
    UserApplicationError,
)
from ..domain.exceptions import (
    EmailEmptyError,
    EmailInvalidFormatError,
    EmailTooLongError,
    HashedPasswordEmptyError,
    HashedPasswordTooLongError,
    UserAlreadyActive,
    UserAlreadyInactive,
    UserCreatedAtInvalidError,
    UserDeactivatedAtInvalidError,
    UserDomainError,
    UserIdInvalidError,
    UserNameEmptyError,
    UserNameTooLongError,
    UserUpdatedAtInvalidError,
)
from ..infrastructure.exceptions import (
    UserInfrastructureError,
    UserNotFoundError,
)
from .handlers import (
    create_application_handler,
    create_domain_handler,
    create_infrastructure_handler,
)

APPLICATION_EXCEPTION_HANDLERS: dict[
    type[UserApplicationError],
    tuple[int, str],
] = {
    EmailAlreadyExistError: (
        status.HTTP_409_CONFLICT,
        "EMAIL_ALREADY_EXIST",
    ),
}

INFRASTRUCTURE_EXCEPTION_HANDLERS: dict[
    type[UserInfrastructureError],
    tuple[int, str],
] = {
    UserNotFoundError: (
        status.HTTP_404_NOT_FOUND,
        "USER_NOT_FOUND",
    ),
}

DOMAIN_EXCEPTION_HANDLERS: dict[
    type[UserDomainError],
    tuple[int, str],
] = {
    UserIdInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_ID_INVALID",
    ),
    EmailEmptyError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_EMAIL_EMPTY",
    ),
    EmailTooLongError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_EMAIL_TOO_LONG",
    ),
    EmailInvalidFormatError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_EMAIL_INVALID_FORMAT",
    ),
    HashedPasswordEmptyError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_HASHED_PASSWORD_EMPTY",
    ),
    HashedPasswordTooLongError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_HASHED_PASSWORD_TOO_LONG",
    ),
    UserNameEmptyError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_NAME_EMPTY",
    ),
    UserNameTooLongError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_NAME_TOO_LONG",
    ),
    UserCreatedAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_CREATE_AT_INVALID",
    ),
    UserUpdatedAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_UPDATED_AT_INVALID",
    ),
    UserDeactivatedAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_DEACTIVATED_AT_INVALID",
    ),
    UserAlreadyActive: (
        status.HTTP_400_BAD_REQUEST,
        "USER_ALREADY_ACTIVE",
    ),
    UserAlreadyInactive: (
        status.HTTP_400_BAD_REQUEST,
        "USER_ALREADY_INACTIVE",
    ),
}


def register_user_exception_handlers(app: FastAPI) -> None:
    for exc_type, (
        status_code,
        error_code,
    ) in APPLICATION_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_application_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )

    for exc_type, (
        status_code,
        error_code,
    ) in INFRASTRUCTURE_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_infrastructure_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )

    for exc_type, (
        status_code,
        error_code,
    ) in DOMAIN_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_domain_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )
