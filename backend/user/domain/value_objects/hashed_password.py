from dataclasses import dataclass

from core.constants import UserConfig

from ..exceptions import (
    HashedPasswordEmptyError,
    HashedPasswordTooLongError,
)


@dataclass(frozen=True)
class HashedPassword:
    value: str

    def __post_init__(self):
        if not self.value:
            raise HashedPasswordEmptyError()

        if len(self.value) > UserConfig.DB_PASSWORD_LENGTH_MAX:
            raise HashedPasswordTooLongError(
                max_length=UserConfig.DB_PASSWORD_LENGTH_MAX,
            )

    def __str__(self) -> str:
        return "***HASHED***"

    def __repr__(self) -> str:
        return "HashedPassword(***)"
