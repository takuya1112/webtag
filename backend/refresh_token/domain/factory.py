from shared.domain.security import TokenGenerator, TokenHasher
from shared.domain.value_objects import AwareDatetime
from user.domain.value_objects import UserId

from .entity import RefreshTokenEntity
from .value_objects import HashedToken


class RefreshTokenFactory:
    def __init__(
        self,
        generator: TokenGenerator,
        hasher: TokenHasher,
    ) -> None:
        self.generator = generator
        self.hasher = hasher

    def create(
        self,
        user_id: UserId,
        expires_at: AwareDatetime,
    ) -> tuple[RefreshTokenEntity, str]:
        raw_token = self.generator.generate()
        hashed_token = HashedToken(self.hasher.hash(raw_token))
        entity = RefreshTokenEntity(
            user_id=user_id,
            token_hash=hashed_token,
            expires_at=expires_at,
        )

        return entity, raw_token
