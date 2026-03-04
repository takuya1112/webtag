from typing import Any


class UserApplicationError(Exception):
    def __init__(self, **params: Any) -> None:
        super().__init__()
        self.params: dict[str, Any] = params


class EmailAlreadyExistError(UserApplicationError):
    pass
