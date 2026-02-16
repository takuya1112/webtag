from shared.domain.clock import Clock
from shared.domain.security import IdGenerator

from .entity import UserEntity
from .value_objects import Email, HashedPassword, UserName


class UserFactory:
    def __init__(self, generator: IdGenerator, clock: Clock) -> None:
        self.generator = generator
        self.clock = clock

    def create(
        self,
        name: UserName,
        email: Email,
        password_hash: HashedPassword,
    ) -> UserEntity:
        id = self.generator.generate()
        now = self.clock.now()
        return UserEntity(
            id=id,
            name=name,
            email=email,
            password_hash=password_hash,
            created_at=now,
            updated_at=now,
            deactivated_at=None,
        )
