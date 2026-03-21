from fastapi import FastAPI, status

from ..application.exceptions import (
    UserApplicationError,
    UserEmailAlreadyExistError,
)
from ..domain.exceptions import (
    UserAlreadyActive,
    UserAlreadyInactive,
    UserCreatedAtInvalidError,
    UserDeactivatedAtInvalidError,
    UserDomainError,
    UserEmailEmptyError,
    UserEmailInvalidFormatError,
    UserEmailTooLongError,
    UserHashedPasswordEmptyError,
    UserHashedPasswordTooLongError,
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
    create_user_application_handler,
    create_user_domain_handler,
    create_user_infrastructure_handler,
)

USER_APPLICATION_EXCEPTION_HANDLERS: dict[
    type[UserApplicationError],
    tuple[int, str],
] = {
    UserEmailAlreadyExistError: (
        status.HTTP_409_CONFLICT,
        "USER_EMAIL_ALREADY_EXIST",
    ),
}

USER_INFRASTRUCTURE_EXCEPTION_HANDLERS: dict[
    type[UserInfrastructureError],
    tuple[int, str],
] = {
    UserNotFoundError: (
        status.HTTP_404_NOT_FOUND,
        "USER_NOT_FOUND",
    ),
}

USER_DOMAIN_EXCEPTION_HANDLERS: dict[
    type[UserDomainError],
    tuple[int, str],
] = {
    UserIdInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_ID_INVALID",
    ),
    UserEmailEmptyError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_EMAIL_EMPTY",
    ),
    UserEmailTooLongError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_EMAIL_TOO_LONG",
    ),
    UserEmailInvalidFormatError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_EMAIL_INVALID_FORMAT",
    ),
    UserHashedPasswordEmptyError: (
        status.HTTP_400_BAD_REQUEST,
        "USER_HASHED_PASSWORD_EMPTY",
    ),
    UserHashedPasswordTooLongError: (
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
    ) in USER_APPLICATION_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_user_application_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )

    for exc_type, (
        status_code,
        error_code,
    ) in USER_INFRASTRUCTURE_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_user_infrastructure_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )

    for exc_type, (
        status_code,
        error_code,
    ) in USER_DOMAIN_EXCEPTION_HANDLERS.items():
        app.add_exception_handler(
            exc_type,
            create_user_domain_handler(
                status_code=status_code,
                error_code=error_code,
            ),
        )
