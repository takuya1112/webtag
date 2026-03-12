from typing import Any


class UserDomainError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class BaseTooLongError(UserDomainError):
    def __init__(self, max_length: int) -> None:
        super().__init__()
        self.max_length = max_length

    @property
    def context(self) -> dict[str, Any]:
        return {"max_length": self.max_length}


class UserAlreadyInactive(UserDomainError):
    pass


class UserAlreadyActive(UserDomainError):
    pass


class UserIdInvalidError(UserDomainError):
    pass


class EmailEmptyError(UserDomainError):
    pass


class EmailTooLongError(BaseTooLongError):
    pass


class EmailInvalidFormatError(UserDomainError):
    pass


class HashedPasswordEmptyError(UserDomainError):
    pass


class HashedPasswordTooLongError(BaseTooLongError):
    pass


class UserNameEmptyError(UserDomainError):
    pass


class UserNameTooLongError(BaseTooLongError):
    pass


class CreatedAtInvalidError(UserDomainError):
    pass


class UpdatedAtInvalidError(UserDomainError):
    pass


class DeactivatedAtInvalidError(UserDomainError):
    pass
