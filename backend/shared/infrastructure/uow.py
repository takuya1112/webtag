from contextlib import contextmanager
from typing import Dict, Generator, Type, TypeVar

from sqlalchemy.orm import Session, sessionmaker

from .session import SessionLocal

T = TypeVar("T")


class UnitOfWork:
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory
        self.session: Session | None = None
        self._repository: Dict[Type, object] = {}

    def __enter__(self) -> "UnitOfWork":
        self.session = self.session_factory()
        self._repository.clear()
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type is not None:
                self.session.rollback()
            else:
                try:
                    self.session.commit()
                except Exception:
                    self.session.rollback()
                    raise
        finally:
            self.session.close()

    def get_repo(self, repository_type: Type[T]) -> T:
        if repository_type not in self._repository:
            self._repository[repository_type] = repository_type(self.session)
        return self._repository[repository_type]


@contextmanager
def get_uow_dependency() -> Generator[UnitOfWork, None, None]:
    with UnitOfWork(SessionLocal) as uow:
        yield uow
