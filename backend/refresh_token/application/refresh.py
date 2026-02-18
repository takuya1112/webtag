from datetime import timedelta

from core.config import settings
from core.logging import get_logger
from shared.application.retry import retry
from shared.domain.security import TokenHasher
from shared.domain.value_objects import AwareDatetime
from shared.infrastructure.clock import Clock

from ..domain.factory import RefreshTokenFactory
from ..domain.repository import RefreshTokenRepository
from ..domain.value_objects import HashedToken
from ..exceptions import InvalidTokenError, TokenAlreadyUsed, TokenStolenError

logger = get_logger(__name__)


class RefreshAccessToken:
    def __init__(
        self,
        repository: RefreshTokenRepository,
        factory: RefreshTokenFactory,
        hasher: TokenHasher,
        clock: Clock,
    ):
        self.repository = repository
        self.factory = factory
        self.hasher = hasher
        self.clock = clock

    @retry()
    def execute(self, refresh_token: str) -> str:
        token_hash_vo = HashedToken(self.hasher.hash(refresh_token))
        entity = self.repository.find_by_hashed_token(token_hash_vo)
        now_vo = AwareDatetime(self.clock.now())

        if not entity:
            logger.warning("Token not exist")
            raise InvalidTokenError("Token not exist")

        try:
            entity.ensure_useable(now_vo)
        except TokenAlreadyUsed:
            logger.error(
                "Token reuse detected, Revoking all tokens for user_id=%s",
                entity.user_id.value,
            )
            self.repository.delete_all_by_user_id(entity.user_id)
            raise TokenStolenError("Token reuse detected") from None

        entity.mark_used(now_vo)
        self.repository.update(entity)

        expires_at_vo = AwareDatetime(
            now_vo.value + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        )
        new_entity, raw_token = self.factory.create(
            user_id=entity.user_id,
            expires_at=expires_at_vo,
        )
        self.repository.add(new_entity)
        logger.debug(
            "Token rotated successfully: user_id=%s",
            entity.user_id.value,
        )
        return raw_token
