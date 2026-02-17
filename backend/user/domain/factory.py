from shared.domain.clock import Clock
from shared.domain.security import IdGenerator
from shared.domain.value_objects import AwareDatetime

from .entity import UserEntity
from .value_objects import Email, HashedPassword, UserId, UserName


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
        id = UserId(self.generator.generate())
        now = AwareDatetime((self.clock.now()))
        return UserEntity(
            id=id,
            name=name,
            email=email,
            password_hash=password_hash,
            created_at=now,
            updated_at=now,
            deactivated_at=None,
        )
