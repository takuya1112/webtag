from datetime import timedelta

from core.config import settings
from core.logging import get_logger
from shared.application.retry import retry
from shared.domain.security import TokenHasher
from shared.domain.value_objects import AwareDatetime
from shared.infrastructure.clock import Clock

from ..domain.factory import RefreshTokenFactory
from ..domain.repository import RefreshTokenRepository
from ..exceptions import TokenAlreadyUsed, TokenStolenError
from .validate import ValidateRefreshToken

logger = get_logger(__name__)


class RefreshAccessToken:
    def __init__(
        self,
        repository: RefreshTokenRepository,
        validator: ValidateRefreshToken,
        factory: RefreshTokenFactory,
        hasher: TokenHasher,
        clock: Clock,
    ):
        self.repository = repository
        self.validator = validator
        self.factory = factory
        self.hasher = hasher
        self.clock = clock

    @retry()
    def execute(self, refresh_token: str) -> str:
        try:
            entity = self.validator.execute(refresh_token)
        except TokenAlreadyUsed as e:
            if e.user_id:
                logger.warning("Token reuse: user_id=%s", e.user_id.value)
                self.repository.delete_all_by_user_id(e.user_id)
                raise TokenStolenError("Token already revoked")

        now_vo = AwareDatetime(self.clock.now())
        entity.mark_used(now_vo)
        self.repository.update(entity)

        expires_at_vo = AwareDatetime(
            now_vo + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        )
        new_entity, raw_token = self.factory.create(
            user_id=entity.user_id,
            expires_at=expires_at_vo,
        )
        self.repository.add(new_entity)
        logger.debug(
            "Token rotated successfully: user_id=%s",
            entity.user_id.value,
        )
        return raw_token
