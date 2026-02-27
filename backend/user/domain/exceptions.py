class UserDomainError(Exception):
    pass


class UserAlreadyInactive(UserDomainError):
    pass


class UserAlreadyActive(UserDomainError):
    pass


class InvalidEmailError(UserDomainError):
    pass


class InvalidHashedPasswordError(UserDomainError):
    pass


class InvalidUserNameError(UserDomainError):
    pass
