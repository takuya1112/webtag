from uuid6 import uuid7

from ...domain.security.id_generator import IdGenerator
from ...domain.value_objects import AppUuid


class UUIDGv7generator(IdGenerator):
    def generate(self) -> AppUuid:
        return AppUuid(uuid7())
