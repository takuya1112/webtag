class SharedDomainError(Exception):
    pass


class InvalidUuidError(SharedDomainError):
    pass


class InvalidAwareDatetimeError(SharedDomainError):
    pass
