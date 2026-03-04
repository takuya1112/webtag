from typing import Any


class UserInfrastructureError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}


class UserNotFoundError(UserInfrastructureError):
    pass
