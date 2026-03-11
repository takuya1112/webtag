from typing import Any

ERROR_MESSAGES = {
    # UUID
    "INVALID_UUID": "UUID is invalid",
    # Aware datetime
    "INVALID_AWARE_DATETIME": "Datetime must be aware",
}


def get_error_message(error_code: str, **params: Any) -> str:
    template = ERROR_MESSAGES[error_code]
    try:
        return template.format(**params)
    except KeyError:
        return template
