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

# user@example.com
# stringst
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmNDdhZjIyZC0zYzdlLTQ4NzUtOGIxOS0wNjljNDUzNDA1MjYiLCJleHAiOjE3NzA2NTMxMjB9.4Z305xs6kuvXJAAmv0wGYIpYo_PlYx-FzgWaz2_QOlI",
#   "token_type": "bearer"
# }