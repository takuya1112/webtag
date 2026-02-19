from uuid import UUID

from uuid6 import uuid7


class UUIDGv7generator:
    def generate(self) -> UUID:
        return uuid7()
