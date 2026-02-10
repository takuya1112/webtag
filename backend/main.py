from fastapi import FastAPI
from api.routers import (
    user, article, tag, article_tag, 
    deleted_article, auth,
)
from core import setup_logging

setup_logging()

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(tag.router)
app.include_router(article_tag.router)
app.include_router(deleted_article.router)
app.include_router(auth.router)

# {
#   "name": "string",
#   "email": "user@example.com",
#   "password": "stringst",
#   "password_repeat": "stringst"
# }