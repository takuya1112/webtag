from shared.domain.clock import Clock
from shared.domain.id_generator import IdGenerator

from .entity import UserEntity
from .value_objects import (
    CreatedAt,
    Email,
    HashedPassword,
    UpdatedAt,
    UserId,
    UserName,
)


class UserFactory:
    def __init__(self, id_generator: IdGenerator, clock: Clock) -> None:
        self.id_generator = id_generator
        self.clock = clock

    def create(
        self,
        name: UserName,
        email: Email,
        password_hash: HashedPassword,
    ) -> UserEntity:
        id = UserId(self.id_generator.generate())
        now = self.clock.now()
        return UserEntity(
            id=id,
            name=name,
            email=email,
            password_hash=password_hash,
            created_at=CreatedAt(now),
            updated_at=UpdatedAt(now),
            deactivated_at=None,
        )
