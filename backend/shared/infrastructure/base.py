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


def get_uow():
    return UnitOfWork(SessionLocal)
