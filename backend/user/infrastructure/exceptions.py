class UserInfrastructureError(Exception):
    pass


class UserNotFoundError(UserInfrastructureError):
    pass
