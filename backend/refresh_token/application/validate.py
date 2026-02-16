from datetime import datetime, timezone

from core.logging import get_logger
from shared.domain.security import TokenHasher

from ..domain.entity import RefreshTokenEntity
from ..domain.repository import RefreshTokenRepository
from ..domain.value_objects import HashedToken
from ..exceptions import (
    ExpiredTokenError,
    InvalidTokenError,
    TokenAlreadyRevoked,
)

logger = get_logger(__name__)


class ValidateRefreshToken:
    def __init__(
        self,
        repository: RefreshTokenRepository,
        hasher: TokenHasher,
    ):
        self.repository = repository
        self.hasher = hasher

    def execute(self, refresh_token: str) -> RefreshTokenEntity:
        hashed_token = HashedToken(self.hasher.hash(refresh_token))
        entity = self.repository.find_by_hashed_token(hashed_token)

        if not entity:
            logger.warning("Token not exist")
            raise InvalidTokenError("Token not exist")

        if entity.is_revoked():
            logger.warning(
                "Token already revoked: user_id=%s", entity.user_id.value
            )
            raise TokenAlreadyRevoked("Token already revoked")

        if entity.is_expired(datetime.now(timezone.utc)):
            logger.warning(
                "Token already expired: user_id=%s", entity.user_id.value
            )
            raise ExpiredTokenError("Token already expired")

        logger.debug(
            "Token validated successfully: user_id=%s", entity.user_id.value
        )
        return entity
