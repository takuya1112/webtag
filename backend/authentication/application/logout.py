from core.logging import get_logger
from refresh_token.domain.refresh_token_hasher import RefreshTokenHasher
from refresh_token.domain.repository import RefreshTokenRepository
from refresh_token.domain.value_objects import RefreshTokenHash, RevokedAt
from shared.application import UnitOfWork
from shared.domain.clock import Clock

from .exceptions import InvalidRefreshTokenError

logger = get_logger(__name__)


class Logout:
    def __init__(
        self,
        uow: UnitOfWork,
        repository: type[RefreshTokenRepository],
        token_hasher: RefreshTokenHasher,
        clock: Clock,
    ):
        self.uow = uow
        self.repository = repository
        self.token_hasher = token_hasher
        self.clock = clock

    def execute(self, refresh_token: str) -> None:
        with self.uow:
            repo = self.uow.get_repo(self.repository)
            token_hash = RefreshTokenHash(self.token_hasher.hash(refresh_token))
            entity = repo.find_by_hashed_token(token_hash)
            if entity is None:
                logger.warning("Refresh token not found")
                raise InvalidRefreshTokenError()

            now = self.clock.now()
            entity.revoke(RevokedAt(now))
            repo.update(entity)

            self.uow.commit()
        logger.info(
            "Refresh token revoked: user_id=%s",
            entity.user_id.value,
        )
