from datetime import timedelta
from uuid import UUID

from core.logging import get_logger
from shared.application import UnitOfWork
from shared.domain.clock import Clock
from user.domain.value_objects import UserId

from ..domain.factory import RefreshTokenFactory
from ..domain.repository import RefreshTokenRepository
from ..domain.value_objects import ExpiredAt

logger = get_logger(__name__)


class CreateRefreshToken:
    def __init__(
        self,
        uow: UnitOfWork,
        repository: type[RefreshTokenRepository],
        factory: RefreshTokenFactory,
        clock: Clock,
        expire_days: int,
    ):
        self.uow = uow
        self.repository = repository
        self.factory = factory
        self.clock = clock
        self.expire_days = expire_days

    # TODO retry and check unique
    def execute(self, user_id: UUID) -> str:
        with self.uow:
            repo = self.uow.get_repo(self.repository)
            user_id_vo = UserId(user_id)
            expires_at_vo = ExpiredAt(
                self.clock.now() + timedelta(days=self.expire_days)
            )
            entity, raw_token = self.factory.create(
                user_id=user_id_vo,
                expires_at=expires_at_vo,
            )
            repo.add(entity)
            self.uow.commit()
        logger.info("entity is added: user_id=%s", entity.user_id.value)
        return raw_token
