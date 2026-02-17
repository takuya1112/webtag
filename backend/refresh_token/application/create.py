from core.logging import get_logger
from shared.application.retry import retry
from shared.domain.value_objects import AppUuid

from ..domain.factory import RefreshTokenFactory
from ..domain.repository import RefreshTokenRepository

logger = get_logger(__name__)


class CreateRefreshToken:
    def __init__(
        self,
        repository: RefreshTokenRepository,
        factory: RefreshTokenFactory,
    ):
        self.repository = repository
        self.factory = factory

    @retry()
    def execute(self, user_id: int) -> str:
        entity, raw_token = self.factory.create(AppUuid(user_id))
        self.repository.add(entity)
        logger.info("entity is added: user_id=%s", entity.user_id.value)
        return raw_token
