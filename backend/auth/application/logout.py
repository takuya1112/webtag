from core.logging import get_logger
from refresh_token.domain.repository import RefreshTokenRepository
from refresh_token.domain.value_objects import HashedToken
from refresh_token.exceptions import InvalidTokenError, TokenAlreadyRevoked
from shared.application import UnitOfWork
from shared.domain.clock import Clock
from shared.domain.security import TokenHasher
from shared.domain.value_objects import AwareDatetime

logger = get_logger(__name__)


class Logout:
    def __init__(
        self,
        uow: UnitOfWork,
        repository: type[RefreshTokenRepository],
        token_hasher: TokenHasher,
        clock: Clock,
    ):
        self.uow = uow
        self.repository = repository
        self.token_hasher = token_hasher
        self.clock = clock

    def execute(self, refresh_token: str) -> None:
        with self.uow:
            repo = self.uow.get_repo(self.repository)
            token_hash = HashedToken(self.token_hasher.hash(refresh_token))
            entity = repo.find_by_hashed_token(token_hash)
            if entity is None:
                logger.warning("Refresh token not found")
                raise InvalidTokenError()
            now_vo = AwareDatetime(self.clock.now())
            try:
                entity.revoke(now_vo)
                repo.update(entity)
            except TokenAlreadyRevoked:
                logger.warning(
                    "Refresh token already revoked: user_id=%s",
                    entity.user_id.value,
                )
                raise InvalidTokenError()
            self.uow.commit()
        logger.info(
            "Refresh token revoked: user_id=%s",
            entity.user_id.value,
        )
