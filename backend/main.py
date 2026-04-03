from article.infrastructure import ArticleModel, ArticleTagModel  # noqa
from authentication.api import router as authentication_router
from core import setup_logging
from fastapi import FastAPI
from refresh_token.api import router as refresh_token_router
from startup.exception_handlers import register_all_exception_handler
from tag.infrastructure.model import TagModel  #  noqa

setup_logging()

app = FastAPI()
register_all_exception_handler(app)
app.include_router(refresh_token_router)
app.include_router(authentication_router)
