class FakeUnitOfWork:
    def __init__(self, repositories: dict):
        self._repositories = repositories
        self.committed = False

    def __enter__(self) -> "FakeUnitOfWork":
        self.committed = False
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if exc_type is not None:
            self.rollback()

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        self.committed = False

    def get_repo(self, repository_type):
        return self._repositories[repository_type]
