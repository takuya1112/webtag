from datetime import datetime, timedelta, timezone

from core.logging import get_logger
from sqlalchemy.orm import Session

from ...domain.entities import RefreshTokenEntity
from ...domain.value_objects import HashedToken, TokenTimestamp, UserId
from ..models import RefreshTokenModel

logger = get_logger(__name__)


class SQLAlchemyRefreshTokenRepository:
    def __init__(self, session: Session):
        self.session = session

    def _to_entity(self, model: RefreshTokenModel) -> RefreshTokenEntity:
        return RefreshTokenEntity(
            user_id=UserId(model.user_id),
            hashed_token=HashedToken(model.hashed_token),
            expires_at=TokenTimestamp(model.expires_at),
            revoked_at=TokenTimestamp(model.revoked_at) if model.revoked_at else None,
        )

    def _to_model(self, entity: RefreshTokenEntity) -> RefreshTokenModel:
        return RefreshTokenModel(
            user_id=entity.user_id.value,
            hashed_token=entity.hashed_token.value,
            expires_at=entity.expires_at.value,
            revoked_at=entity.revoked_at.value if entity.revoked_at else None,
        )

    def save(self, token: RefreshTokenEntity) -> None:
        model = self._to_model(token)
        self.session.merge(model)
        logger.info("token saved successfully")

    def find_by_user_id(self, user_id: UserId) -> list[RefreshTokenEntity]:
        models = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.user_id == user_id.value)
            .all()
        )
        return [self._to_entity(model) for model in models]

    def find_by_hashed_token(
        self,
        hashed_token: HashedToken,
    ) -> RefreshTokenEntity | None:
        model = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.hashed_token == hashed_token.value)
            .one_or_none()
        )
        return self._to_entity(model) if model else None

    def delete_all_by_user_id(self, user_id: UserId) -> None:
        count = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.user_id == user_id.value)
            .delete()
        )
        logger.info("Deleted %s tokens", count)

    def delete_by_hashed_token(self, hashed_token: HashedToken) -> None:
        self.session.query(RefreshTokenModel).filter(
            RefreshTokenModel.hashed_token == hashed_token.value
        ).delete()

    def delete_expired_tokens(self) -> None:
        now = datetime.now(timezone.utc)
        count = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.expires_at <= now)
            .delete()
        )
        logger.info("Deleted %s expired tokens", count)

    def delete_old_revoked_tokens(self) -> None:
        cutoff = datetime.now(timezone.utc) - timedelta(days=30)
        count = (
            self.session.query(RefreshTokenModel)
            .filter(
                RefreshTokenModel.revoked_at.isnot(None),
                RefreshTokenModel.revoked_at < cutoff,
            )
            .delete()
        )
        logger.info("Deleted %s old revoked tokens", count)
