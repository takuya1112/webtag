class UserDomainError(Exception):
    pass


class UserAlreadyInactive(UserDomainError):
    pass


class UserAlreadyActive(UserDomainError):
    pass
