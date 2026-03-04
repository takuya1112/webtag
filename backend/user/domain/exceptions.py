from typing import Any


class UserDomainError(Exception):
    def __init__(self, **params: Any) -> None:
        super().__init__()
        self.params: dict[str, Any] = params


class UserAlreadyInactive(UserDomainError):
    pass


class UserAlreadyActive(UserDomainError):
    pass


class EmailEmptyError(UserDomainError):
    pass


class EmailTooLongError(UserDomainError):
    def __init__(self, max_length: int) -> None:
        super().__init__(max_length=max_length)


class EmailInvalidFormatError(UserDomainError):
    pass


class HashedPasswordEmptyError(UserDomainError):
    pass


class HashedPasswordTooLongError(UserDomainError):
    def __init__(self, max_length: int) -> None:
        super().__init__(max_length=max_length)


class UserNameEmptyError(UserDomainError):
    pass


class UserNameTooLongError(UserDomainError):
    def __init__(self, max_length: int) -> None:
        super().__init__(max_length=max_length)
