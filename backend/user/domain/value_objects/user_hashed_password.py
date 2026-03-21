from dataclasses import dataclass

from core.constants import UserConfig

from ..exceptions import (
    UserHashedPasswordEmptyError,
    UserHashedPasswordTooLongError,
)


@dataclass(frozen=True)
class UserHashedPassword:
    value: str

    def __post_init__(self):
        if not self.value:
            raise UserHashedPasswordEmptyError()

        if len(self.value) > UserConfig.DB_PASSWORD_LENGTH_MAX:
            raise UserHashedPasswordTooLongError(
                max_length=UserConfig.DB_PASSWORD_LENGTH_MAX,
            )

    def __str__(self) -> str:
        return "***HASHED***"

    def __repr__(self) -> str:
        return "HashedPassword(***)"
