from dataclasses import dataclass

from core.constants import UserConfig

from ...exceptions.domain import InvalidHashedPasswordError


@dataclass(frozen=True)
class HashedPassword:
    value: str

    def __post_init__(self):
        if not self.value:
            raise InvalidHashedPasswordError("HashedPassword must be filled")

        if len(self.value) > UserConfig.DB_PASSWORD_LENGTH_MAX:
            raise InvalidHashedPasswordError("HashedPassword is too long")

    def __str__(self) -> str:
        return "***HASHED***"

    def __repr__(self) -> str:
        return "HashedPassword(***)"
