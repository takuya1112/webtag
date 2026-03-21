from typing import Any

ERROR_MESSAGES = {
    # jwt service
    "EXPIRED_ACCESS_TOKEN": "Access token has Expired",
    "INVALID_ACCESS_TOKEN": "Access token is invalid",
}


def get_error_message(error_code: str, **params: Any) -> str:
    template = ERROR_MESSAGES[error_code]
    try:
        return template.format(**params)
    except KeyError:
        return template
