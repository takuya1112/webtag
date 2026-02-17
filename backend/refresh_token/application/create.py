from datetime import timedelta

from core.config import settings
from core.logging import get_logger
from shared.application.retry import retry
from shared.domain.clock import Clock
from shared.domain.value_objects import AwareDatetime
from user.domain.value_objects import UserId

from ..domain.factory import RefreshTokenFactory
from ..domain.repository import RefreshTokenRepository

logger = get_logger(__name__)


class CreateRefreshToken:
    def __init__(
        self,
        repository: RefreshTokenRepository,
        factory: RefreshTokenFactory,
        clock: Clock,
    ):
        self.repository = repository
        self.factory = factory
        self.clock = clock

    @retry()
    def execute(self, user_id: int) -> str:
        user_id_vo = UserId(user_id)
        expires_at_vo = AwareDatetime(
            self.clock.now()
            + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        )
        entity, raw_token = self.factory.create(
            user_id=user_id_vo,
            expires_at=expires_at_vo,
        )
        self.repository.add(entity)
        logger.info("entity is added: user_id=%s", entity.user_id.value)
        return raw_token
