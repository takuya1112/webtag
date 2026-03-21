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


class UserEmailEmptyError(UserDomainError):
    pass


class UserEmailTooLongError(BaseTooLongError):
    pass


class UserEmailInvalidFormatError(UserDomainError):
    pass


class UserHashedPasswordEmptyError(UserDomainError):
    pass


class UserHashedPasswordTooLongError(BaseTooLongError):
    pass


class UserNameEmptyError(UserDomainError):
    pass


class UserNameTooLongError(BaseTooLongError):
    pass


class UserCreatedAtInvalidError(UserDomainError):
    pass


class UserUpdatedAtInvalidError(UserDomainError):
    pass


class UserDeactivatedAtInvalidError(UserDomainError):
    pass
