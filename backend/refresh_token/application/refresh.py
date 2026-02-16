from datetime import datetime, timezone

from core.logging import get_logger
from shared.application.retry import retry
from shared.domain.security import TokenHasher

from ..domain.factory import RefreshTokenFactory
from ..domain.repository import RefreshTokenRepository
from ..domain.value_objects import HashedToken
from ..exceptions import ExpiredTokenError, InvalidTokenError, TokenStolenError

logger = get_logger(__name__)


class RefreshAccessToken:
    def __init__(
        self,
        repository: RefreshTokenRepository,
        factory: RefreshTokenFactory,
        hasher: TokenHasher,
    ):
        self.repository = repository
        self.factory = factory
        self.hasher = hasher

    @retry()
    def execute(self, refresh_token: str) -> str:
        hashed_token = HashedToken(self.hasher.hash(refresh_token))
        entity = self.repository.find_by_hashed_token(hashed_token)

        if not entity:
            logger.warning("Token not exist")
            raise InvalidTokenError("Token not exist")

        if entity.is_revoked():
            logger.warning("Token reuse: user_id=%s", entity.user_id.value)
            self.repository.delete_all_by_user_id(entity.user_id)
            raise TokenStolenError("Token already revoked")

        if entity.is_expired(datetime.now(timezone.utc)):
            logger.warning(
                "Token already expired: user_id=%s", entity.user_id.value
            )
            raise ExpiredTokenError("Token already expired")

        entity.revoke(datetime.now(timezone.utc))
        self.repository.update(entity)

        new_entity, raw_token = self.factory.create(entity.user_id)
        self.repository.add(new_entity)
        logger.debug(
            "Token rotated successfully: user_id=%s", entity.user_id.value
        )
        return raw_token
