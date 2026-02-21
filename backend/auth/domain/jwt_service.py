from typing import Protocol
from uuid import UUID


class JwtService(Protocol):
    def issue(self, user_id: UUID) -> str: ...
    def verify(self, token: str) -> UUID | None: ...
