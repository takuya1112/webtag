from typing import Any

ACCESS_TOKEN_ERROR_MESSAGES = {
    # jwt service
    "EXPIRED_ACCESS_TOKEN": "Access token is Expired",
    "INVALID_ACCESS_TOKEN": "Access token is invalid",
}


def get_access_token_error_message(error_code: str, **params: Any) -> str:
    template = ACCESS_TOKEN_ERROR_MESSAGES[error_code]
    try:
        return template.format(**params)
    except KeyError:
        return template
