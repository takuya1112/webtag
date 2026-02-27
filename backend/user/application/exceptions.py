class UserApplicationError(Exception):
    pass


class EmailAlreadyExistError(UserApplicationError):
    pass
