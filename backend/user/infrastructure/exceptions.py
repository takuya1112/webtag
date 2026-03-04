from typing import Any


class UserInfrastructureError(Exception):
    def __init__(self, **params: Any) -> None:
        super().__init__()
        self.params: dict[str, Any] = params


class UserNotFoundError(UserInfrastructureError):
    pass
