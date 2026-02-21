from auth.api import router as auth_router
from core import setup_logging
from fastapi import FastAPI
from refresh_token.api import router as refresh_token_router
from shared.api import register_exception_handler

setup_logging()

app = FastAPI()
register_exception_handler(app)
app.include_router(refresh_token_router)
app.include_router(auth_router)
