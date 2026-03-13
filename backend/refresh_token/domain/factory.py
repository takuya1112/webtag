from shared.domain.clock import Clock
from shared.domain.id_generator import IdGenerator
from shared.domain.value_objects import AwareDatetime
from user.domain.value_objects import UserId

from .entity import RefreshTokenEntity
from .refresh_token_generator import RefreshTokenGenerator
from .refresh_token_hasher import RefreshTokenHasher
from .value_objects import RefreshTokenHash, RefreshTokenId


class RefreshTokenFactory:
    def __init__(
        self,
        token_generator: RefreshTokenGenerator,
        token_hasher: RefreshTokenHasher,
        id_generator: IdGenerator,
        clock: Clock,
    ) -> None:
        self.token_generator = token_generator
        self.token_hasher = token_hasher
        self.id_generator = id_generator
        self.clock = clock

    def create(
        self,
        user_id: UserId,
        expires_at: AwareDatetime,
    ) -> tuple[RefreshTokenEntity, str]:
        id = RefreshTokenId(self.id_generator.generate())
        raw_token = self.token_generator.generate()
        token_hash = RefreshTokenHash(self.token_hasher.hash(raw_token))
        now = AwareDatetime(self.clock.now())
        entity = RefreshTokenEntity(
            id=id,
            user_id=user_id,
            token_hash=token_hash,
            created_at=now,
            expires_at=expires_at,
        )
        return entity, raw_token
