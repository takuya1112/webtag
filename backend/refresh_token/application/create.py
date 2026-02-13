from core.logging import get_logger

from ..domain.factory import RefreshTokenFactory
from ..domain.repository import RefreshTokenRepository
from ..domain.value_objects import UserId

logger = get_logger(__name__)


class CreateRefreshToken:
    def __init__(
        self,
        factory: RefreshTokenFactory,
        repository: RefreshTokenRepository,
    ):
        self.factory = factory
        self.repository = repository

    def execute(self, user_id: int) -> str:
        entity, raw_token = self.factory.create(UserId(user_id))
        self.repository.add(entity)
        logger.info(
            "create and add refresh token",
            extra={
                "event": "create and add new refresh token",
            },
        )
        return raw_token
