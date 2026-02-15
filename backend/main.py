from core import setup_logging
from fastapi import FastAPI
from refresh_token.api import router

setup_logging()

app = FastAPI()
app.include_router(router)
