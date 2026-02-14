from datetime import datetime, timedelta, timezone

from core.config import settings
from core.logging import get_logger
from sqlalchemy.orm import Session

from ..domain import RefreshTokenEntity
from ..domain.value_objects import HashedToken, TokenTimestamp, UserId
from ..exceptions import TokenNotFoundError
from .model import RefreshTokenModel

logger = get_logger(__name__)


class SQLAlchemyRefreshTokenRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, token: RefreshTokenEntity) -> None:
        """Add a refresh token

        Args:
            token (RefreshTokenEntity): The refresh token to add
        """
        model = self._to_model(token)
        self.session.add(model)
        logger.info("Token added")

    def update(self, token: RefreshTokenEntity) -> None:
        """Update a refresh token

        Args:
            token (RefreshTokenEntity): The refresh token to update

        Raises:
            TokenNotFoundError: if none found
        """
        model = self._get_model_by_hashed_token(token.hashed_token)
        model.expires_at = token.expires_at.value
        model.revoked_at = token.revoked_at.value if token.revoked_at else None
        logger.info("Token updated successfully")

    def find_by_user_id(self, user_id: UserId) -> list[RefreshTokenEntity]:
        """Find all refresh tokens by user id

        Args:
            user_id (UserId): user id to find

        Returns:
            list[RefreshTokenEntity]: Return empty list, if none found
        """
        models = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.user_id == user_id.value)
            .all()
        )
        logger.debug("Found %s tokens by user_id", len(models))
        return [self._to_entity(model) for model in models]

    def find_by_hashed_token(
        self,
        hashed_token: HashedToken,
    ) -> RefreshTokenEntity | None:
        """Find a refresh token by hashed token

        Args:
            hashed_token (HashedToken): hashed token to find

        Returns:
            RefreshTokenEntity | None: Return None, if none found
        """
        model = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.hashed_token == hashed_token.value)
            .one_or_none()
        )
        if model:
            logger.debug("Token found by hashed token")
        else:
            logger.debug("Token not found by hashed token")
        return self._to_entity(model) if model else None

    def delete_all_by_user_id(self, user_id: UserId) -> int:
        """Delete all refresh tokens by user id

        Args:
            user_id (UserId): user id

        Returns:
            int: delete count
        """
        delete_count = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.user_id == user_id.value)
            .delete()
        )
        logger.info("Deleted %s tokens by user_id", delete_count)
        return delete_count

    def delete_by_hashed_token(self, hashed_token: HashedToken) -> int:
        """Delete refresh token by hashed token

        Args:
            hashed_token (HashedToken): hashed token to delete

        Returns:
            int: delete count
        """
        delete_count = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.hashed_token == hashed_token.value)
            .delete()
        )
        logger.info("Deleted %s tokens by hashed token", delete_count)
        return delete_count

    def delete_expired_tokens(self) -> int:
        """Deletes all expired refresh tokens

        Returns:
            int: delete count
        """
        now = datetime.now(timezone.utc)
        delete_count = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.expires_at <= now)
            .delete()
        )
        logger.info("Deleted %s expired tokens", delete_count)
        return delete_count

    def delete_old_revoked_tokens(self) -> int:
        """Deletes all old revoked tokens

        Returns:
            int: delete count
        """
        cutoff = datetime.now(timezone.utc) - timedelta(
            days=settings.REVOKED_REFRESH_TOKEN_EXPIRE_DAYS
        )
        delete_count = (
            self.session.query(RefreshTokenModel)
            .filter(
                RefreshTokenModel.revoked_at.isnot(None),
                RefreshTokenModel.revoked_at < cutoff,
            )
            .delete()
        )
        logger.info("Deleted %s old revoked tokens", delete_count)
        return delete_count

    def _get_model_by_hashed_token(
        self,
        hashed_token: HashedToken,
    ) -> RefreshTokenModel:
        """Get a SQLAlchemy model by hashed token

        Args:
            hashed_token (HashedToken): hashed token to find

        Raises:
            TokenNotFoundError: if none found

        Returns:
            RefreshTokenModel: SQLAlchemy model
        """
        model = (
            self.session.query(RefreshTokenModel)
            .filter(RefreshTokenModel.hashed_token == hashed_token.value)
            .one_or_none()
        )
        if model is None:
            logger.warning("Token not found")
            raise TokenNotFoundError("Token not found")
        return model

    def _to_entity(self, model: RefreshTokenModel) -> RefreshTokenEntity:
        """SQLAlchemy model -> Domain entity"""
        return RefreshTokenEntity(
            user_id=UserId(model.user_id),
            hashed_token=HashedToken(model.hashed_token),
            expires_at=TokenTimestamp(model.expires_at),
            revoked_at=TokenTimestamp(model.revoked_at)
            if model.revoked_at
            else None,
        )

    def _to_model(self, entity: RefreshTokenEntity) -> RefreshTokenModel:
        """Domain entity -> SQLAlchemy model"""
        return RefreshTokenModel(
            user_id=entity.user_id.value,
            hashed_token=entity.hashed_token.value,
            expires_at=entity.expires_at.value,
            revoked_at=entity.revoked_at.value if entity.revoked_at else None,
        )
