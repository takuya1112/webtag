from typing import Any


class AccessTokenInfrastructureError(Exception):
    @property
    def context(self) -> dict[str, Any]:
        return {}
