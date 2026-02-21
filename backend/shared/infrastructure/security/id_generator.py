from uuid import UUID

from uuid6 import uuid7


class UUIDv7generator:
    def generate(self) -> UUID:
        return uuid7()
