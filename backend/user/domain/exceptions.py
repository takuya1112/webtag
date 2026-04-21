from typing import Any


class UserDomainError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }


class UserBaseTooLongError(UserDomainError):
    def __init__(self, max_length: int) -> None:
        super().__init__()
        self.max_length = max_length


class UserAlreadyInactive(UserDomainError):
    pass


class UserAlreadyActive(UserDomainError):
    pass


class UserIdInvalidError(UserDomainError):
    pass


class EmailEmptyError(UserDomainError):
    pass


class EmailTooLongError(UserBaseTooLongError):
    pass


class EmailInvalidFormatError(UserDomainError):
    pass


class HashedPasswordEmptyError(UserDomainError):
    pass


class HashedPasswordTooLongError(UserBaseTooLongError):
    pass


class UserNameEmptyError(UserDomainError):
    pass


class UserNameTooLongError(UserBaseTooLongError):
    pass


class UserCreatedAtInvalidError(UserDomainError):
    pass


class UserUpdatedAtInvalidError(UserDomainError):
    pass


class UserDeactivatedAtInvalidError(UserDomainError):
    pass
