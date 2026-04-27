from typing import Any

ERROR_MESSAGES = {
    # Article id
    "ARTICLE_ID_INVALID": "Article id is invalid",
    # Article tile
    "ARTICLE_TITLE_EMPTY": "Article title must be filled",
    "ARTICLE_TITLE_TOO_LONG": "Article title is too long (max: {max_length} characters)",
    # Url
    "ARTICLE_URL_EMPTY": "Url must be filled",
    "ARTICLE_URL_INVALID_FORMAT": "Invalid url format",
    "ARTICLE_URL_TOO_LONG": "Url is too long (max: {max_length} characters)",
    # Created at
    "ARTICLE_CREATED_AT_INVALID": "Created at must be timezone-aware",
    # Updated at
    "ARTICLE_UPDATED_AT_INVALID": "Updated at must be timezone-aware",
    # Deleted at
    "ARTICLE_DELETED_AT_INVALID": "Deleted at must be timezone-aware",
    # Article Entity
    "ARTICLE_ALREADY_DELETED": "Article already deleted",
    "ARTICLE_NOT_DELETED": "Article not deleted",
}


def get_error_message(error_code: str, **params: Any) -> str:
    template = ERROR_MESSAGES[error_code]
    try:
        return template.format(**params)
    except KeyError:
        return template
