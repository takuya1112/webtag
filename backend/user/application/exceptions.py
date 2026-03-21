from typing import Any


class UserApplicationError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class UserEmailAlreadyExistError(UserApplicationError):
    pass
