class AuthenticationApplicationError(Exception):
    pass


class UserUnauthorizedError(AuthenticationApplicationError):
    pass
