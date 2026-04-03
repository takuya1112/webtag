from typing import Any

ERROR_MESSAGES = {
    # Application
    "INVALID_CREDENTIALS": "Invalid password or email",
    "INVALID_REFRESH_TOKEN": "Invalid refresh token",
    "USER_UNAUTHORIZE": "User unauthorize",
}


def get_error_message(error_code: str, **params: Any) -> str:
    template = ERROR_MESSAGES[error_code]
    try:
        return template.format(**params)
    except KeyError:
        return template
