from fastapi import FastAPI, status

from ..application.exceptions import (
    ArticleApplicationError,
)
from ..domain.exceptions import (
    ArticleAlreadyDeletedError,
    ArticleCreatedAtInvalidError,
    ArticleDeletedAtInvalidError,
    ArticleDomainError,
    ArticleIdInvalidError,
    ArticleNotDeletedError,
    ArticleTitleEmptyError,
    ArticleTitleTooLongError,
    ArticleUpdatedAtInvalidError,
    ArticleUrlEmptyError,
    ArticleUrlInvalidFormatError,
    ArticleUrlTooLongError,
)
from ..infrastructure.exceptions import (
    ArticleInfrastructureError,
)
from .handlers import (
    create_application_handler,
    create_domain_handler,
    create_infrastructure_handler,
)

APPLICATION_EXCEPTION_HANDLERS: dict[
    type[ArticleApplicationError],
    tuple[int, str],
] = {}


INFRASTRUCTURE_EXCEPTION_HANDLERS: dict[
    type[ArticleInfrastructureError], tuple[int, str]
] = {}


DOMAIN_EXCEPTION_HANDLERS: dict[type[ArticleDomainError], tuple[int, str]] = {
    ArticleIdInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_ID_INVALID",
    ),
    ArticleTitleEmptyError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_TITLE_EMPTY",
    ),
    ArticleTitleTooLongError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_TITLE_TOO_LONG",
    ),
    ArticleUrlEmptyError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_URL_EMPTY",
    ),
    ArticleUrlInvalidFormatError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_URL_INVALID_FORMAT",
    ),
    ArticleUrlTooLongError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_URL_TOO_LONG",
    ),
    ArticleCreatedAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_CREATED_AT_INVALID",
    ),
    ArticleUpdatedAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_UPDATED_AT_INVALID",
    ),
    ArticleDeletedAtInvalidError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_DELETED_AT_INVALID",
    ),
    ArticleAlreadyDeletedError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_ALREADY_DELETED",
    ),
    ArticleNotDeletedError: (
        status.HTTP_400_BAD_REQUEST,
        "ARTICLE_NOT_DELETED",
    ),
}


def register_article_exception_handlers(app: FastAPI) -> None:
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
