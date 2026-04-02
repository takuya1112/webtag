from typing import Any

ERROR_MESSAGES = {
    # Application
    "INVALID_REFRESH_TOKEN": "Invalid refresh token",
    "TOKEN_STOLEN": "Token may have been stolen",
    # Infrastructure
    "REFRESH_TOKEN_NOT_FOUND": "Refresh token not found",
    # Refresh token hash
    "REFRESH_TOKEN_HASH_EMPTY": "Refresh token hash must be filled",
    # Created at
    "REFRESH_TOKEN_CREATED_AT_INVALID": "Created at must be timezone-aware",
    # Expired at
    "REFRESH_TOKEN_EXPIRED_AT_INVALID": "Expired at must be timezone-aware",
    # Used at
    "REFRESH_TOKEN_USED_AT_INVALID": "Used at must be timezone-aware",
    # Revoked at
    "REFRESH_TOKEN_REVOKED_AT_INVALID": "Revoked at must be timezone-aware",
    # Refresh Token Entity
    "REFRESH_TOKEN_EXPIRED": "Refresh token has expired",
    "REFRESH_TOKEN_ALREADY_USED": "Refresh token has already been used",
    "REFRESH_TOKEN_ALREADY_REVOKED": "Refresh token has already been revoked",
}


def get_error_message(error_code: str, **params: Any) -> str:
    template = ERROR_MESSAGES[error_code]
    try:
        return template.format(**params)
    except KeyError:
        return template
