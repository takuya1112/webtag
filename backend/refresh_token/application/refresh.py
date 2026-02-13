from datetime import datetime, timezone

from core.logging import get_logger
from core.security import TokenHasher

from ..domain.factory import RefreshTokenFactory
from ..domain.repository import RefreshTokenRepository
from ..domain.value_objects import HashedToken, UserId
from ..exceptions import ExpiredTokenError, InvalidTokenError, TokenAlreadyRevoked

logger = get_logger(__name__)


class RefreshAccessToken:
    def __init__(
        self,
        factory: RefreshTokenFactory,
        repository: RefreshTokenRepository,
        token_hasher: TokenHasher,
    ):
        self.factory = factory
        self.repository = repository
        self.token_hasher = token_hasher

    def execute(self, refresh_token: str) -> str:
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

        entity.revoke(datetime.now(timezone.utc))
        self.repository.update(entity)

        new_entity, raw_token = self.factory.create(UserId(entity.user_id))
        self.repository.add(new_entity)
        return raw_token
