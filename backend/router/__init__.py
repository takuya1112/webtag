from .article import article_router
from .deleted_article import deleted_article_router
from .tag import tag_router
from .article_tag import article_tag_router

__all__ = [
    "article_router",
    "deleted_article_router",
    "tag_router",
    "article_tag_router"
    ]