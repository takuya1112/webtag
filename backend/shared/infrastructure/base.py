from contextlib import contextmanager
from typing import Generator

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .uow import UnitOfWork

engine = create_engine(settings.database_url, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


@contextmanager
def get_uow_dependency() -> Generator:
    with UnitOfWork(SessionLocal) as uow:
        yield uow
