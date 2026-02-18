from core.logging import get_logger
from shared.domain.security import TokenHasher
from shared.domain.value_objects import AwareDatetime
from shared.infrastructure.clock import Clock

from ..domain.entity import RefreshTokenEntity
from ..domain.repository import RefreshTokenRepository
from ..domain.value_objects import HashedToken
from ..exceptions import (
    ExpiredTokenError,
    InvalidTokenError,
    TokenAlreadyRevoked,
    TokenAlreadyUsed,
)

logger = get_logger(__name__)


class ValidateRefreshToken:
    def __init__(
        self,
        repository: RefreshTokenRepository,
        hasher: TokenHasher,
        clock: Clock,
    ):
        self.repository = repository
        self.hasher = hasher
        self.clock = clock

    def execute(self, refresh_token: str) -> RefreshTokenEntity:
        token_hash_vo = HashedToken(self.hasher.hash(refresh_token))
        entity = self.repository.find_by_hashed_token(token_hash_vo)
        now_vo = AwareDatetime(self.clock.now())

        if not entity:
            logger.warning("Token not exist")
            raise InvalidTokenError("Token not exist")

        if entity.is_revoked():
            logger.warning(
                "Token already revoked: user_id=%s",
                entity.user_id.value,
            )
            raise TokenAlreadyRevoked("Token already revoked")

        if entity.is_used():
            logger.warning(
                "Token already used: user_id=%s",
                entity.user_id.value,
            )
            raise TokenAlreadyUsed("Token already used", user_id=entity.user_id)

        if entity.is_expired(now_vo):
            logger.warning(
                "Token already expired: user_id=%s",
                entity.user_id.value,
            )
            raise ExpiredTokenError("Token already expired")

        logger.debug(
            "Token validated successfully: user_id=%s",
            entity.user_id.value,
        )
        return entity
