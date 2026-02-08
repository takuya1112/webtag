# from backend.db import get_session
# from backend.db.services import *

# with get_session() as session:
#     with session.begin():
#         a = ArticleSearchService(session)
#         print(a.search(["woman"]))
        

from fastapi import FastAPI
from api.routers import *
from core import setup_logging

setup_logging()

app = FastAPI()
app.include_router(user.router)