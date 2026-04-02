from datetime import timedelta

from core.logging import get_logger
from shared.application import UnitOfWork
from shared.domain.clock import Clock

from ..domain.exceptions import (
    RefreshTokenAlreadyUsed,
    RefreshTokenDomainError,
)
from ..domain.factory import RefreshTokenFactory
from ..domain.refresh_token_hasher import RefreshTokenHasher
from ..domain.repository import RefreshTokenRepository
from ..domain.value_objects import RefreshTokenHash, expires_at
from .exceptions import (
    InvalidTokenError,
    TokenStolenError,
)

logger = get_logger(__name__)


class RefreshAccessToken:
    def __init__(
        self,
        uow: UnitOfWork,
        repository: type[RefreshTokenRepository],
        factory: RefreshTokenFactory,
        hasher: RefreshTokenHasher,
        clock: Clock,
        expire_days: int,
    ):
        self.uow = uow
        self.repository = repository
        self.factory = factory
        self.hasher = hasher
        self.clock = clock
        self.expire_days = expire_days

    # TODO retry and check unique
    def execute(self, refresh_token: str) -> str:
        with self.uow:
            repo = self.uow.get_repo(self.repository)
            token_hash_vo = RefreshTokenHash(self.hasher.hash(refresh_token))
            now_vo = expires_at(self.clock.now())
            entity = repo.find_by_hashed_token(token_hash_vo)

            if not entity:
                logger.warning("Token not exist")
                raise InvalidTokenError()

            try:
                entity.ensure_useable(now_vo)
            except RefreshTokenAlreadyUsed:
                logger.error(
                    "Token reuse detected, Revoking all tokens for user_id=%s",
                    entity.user_id.value,
                )
                repo.delete_all_by_user_id(entity.user_id)
                raise TokenStolenError() from None
            except RefreshTokenDomainError:
                logger.warning(
                    "Invalid token: user_id=%s",
                    entity.user_id.value,
                )
                raise InvalidTokenError() from None

            entity.mark_used(now_vo)
            repo.update(entity)

            expires_at_vo = expires_at(
                now_vo.value + timedelta(days=self.expire_days)
            )
            new_entity, raw_token = self.factory.create(
                user_id=entity.user_id,
                expires_at=expires_at_vo,
            )
            repo.add(new_entity)
            self.uow.commit()
        logger.debug(
            "Token rotated successfully: user_id=%s",
            entity.user_id.value,
        )
        return raw_token
