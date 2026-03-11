from typing import Protocol


class RefreshTokenHasher(Protocol):
    def hash(self, token: str) -> str: ...

    def verify(self, token: str, hashed_token: str) -> bool: ...
