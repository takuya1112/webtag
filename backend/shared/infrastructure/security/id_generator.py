from uuid import UUID

from uuid6 import uuid7

from ...domain.security.id_generator import IdGenerator


class UUIDGv7generator(IdGenerator):
    def generate(self) -> UUID:
        return uuid7()
