from typing import Any


class UserApplicationError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }


class EmailAlreadyExistError(UserApplicationError):
    pass
