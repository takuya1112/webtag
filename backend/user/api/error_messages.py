from typing import Any

ERROR_MESSAGES = {
    # Application
    "EMAIL_ALREADY_EXIST": "Email already exists",
    # Infrastructure
    "USER_NOT_FOUND": "User not found",
    # User id
    "USER_ID_INVALID": "User id is invalid",
    # User name
    "USER_NAME_EMPTY": "User name must be filled",
    "USER_NAME_TOO_LONG": "User name is too long (max: {max_length} characters)",
    # Email
    "EMAIL_EMPTY": "Email must be filled",
    "EMAIL_TOO_LONG": "Email is too long (max: {max_length} characters)",
    "EMAIL_INVALID_FORMAT": "Invalid email format",
    # Hashed password
    "HASHED_PASSWORD_EMPTY": "Hashed password must be filled",
    "HASHED_PASSWORD_TOO_LONG": "Hashed password is too long (max: {max_length} characters)",
    # Created at
    "CREATE_At_INVALID": "Created at must be timezone-aware",
    # Updated at
    "UPDATED_At_INVALID": "Updated at must be timezone-aware",
    # Deactivated at
    "DEACTIVATED_At_INVALID": "Deactivated at must be timezone-aware",
    # User Entity
    "USER_ALREADY_ACTIVE": "User is already active",
    "USER_ALREADY_INACTIVE": "User is already inactive",
}


def get_error_message(error_code: str, **params: Any) -> str:
    template = ERROR_MESSAGES[error_code]
    try:
        return template.format(**params)
    except KeyError:
        return template
