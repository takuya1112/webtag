from datetime import datetime, timedelta, timezone

from core.config import settings
from core.security import TokenGenerator, TokenHasher

from .entity import RefreshTokenEntity
from .value_objects import HashedToken, TokenTimestamp, UserId


class RefreshTokenFactory:
    def __init__(
        self,
        generator: TokenGenerator,
        hasher: TokenHasher,
    ) -> None:
        self.generator = generator
        self.hasher = hasher

    def create(self, user_id: UserId) -> tuple[RefreshTokenEntity, str]:
        raw_token = self.generator.generate()
        hashed_token = self.hasher.hash(raw_token)

        expires_at = datetime.now(timezone.utc) + timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS
        )

        entity = RefreshTokenEntity(
            user_id=user_id,
            hashed_token=HashedToken(hashed_token),
            expires_at=TokenTimestamp(expires_at),
        )

        return entity, raw_token
