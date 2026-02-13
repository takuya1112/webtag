from datetime import datetime, timezone

from core.logging import get_logger
from core.security import TokenHasher

from ..domain.entity import RefreshTokenEntity
from ..domain.repository import RefreshTokenRepository
from ..domain.value_objects import HashedToken
from ..exceptions import ExpiredTokenError, InvalidTokenError, TokenAlreadyRevoked

logger = get_logger(__name__)


class ValidateRefreshToken:
    def __init__(
        self,
        repository: RefreshTokenRepository,
        token_hasher: TokenHasher,
    ):
        self.repository = repository
        self.token_hasher = token_hasher

    def execute(self, refresh_token: str) -> RefreshTokenEntity:
        hashed_token = HashedToken(self.token_hasher.hash(refresh_token))
        entity = self.repository.find_by_hashed_token(hashed_token)
        if not entity:
            logger.warning("Token not exist")
            raise InvalidTokenError("Token not exist")
        if entity.is_revoked():
            logger.warning("Token already revoked")
            raise TokenAlreadyRevoked("Token already revoked")
        if entity.is_expired(datetime.now(timezone.utc)):
            logger.warning("Token already expired")
            raise ExpiredTokenError("Token already expired")

        logger.debug()
        return entity
