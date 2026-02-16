from datetime import datetime, timezone
from uuid import uuid4

from shared.domain.value_objects import AwareDatetime, PublicId

from .entity import UserEntity
from .value_objects import Email, HashedPassword, UserName


class UserFactory:
    def create(
        self,
        name: UserName,
        email: Email,
        password_hash: HashedPassword,
    ) -> UserEntity:
        public_id = PublicId(uuid4())
        now = AwareDatetime(datetime.now(timezone.utc))
        return UserEntity(
            public_id=public_id,
            name=name,
            email=email,
            password_hash=password_hash,
            created_at=now,
            updated_at=now,
            deactivated_at=None,
        )
