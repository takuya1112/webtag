from core.logging import get_logger
from shared.domain.value_objects import AwareDatetime
from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from user.domain.value_objects import UserId

from ..domain import RefreshTokenEntity
from ..domain.value_objects import HashedToken, RefreshTokenId
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
        model = self._get_model_by_hashed_token_or_raise(token.token_hash)
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
        stmt = select(RefreshTokenModel).where(
            RefreshTokenModel.user_id == user_id.value
        )
        models = self.session.scalars(stmt).all()
        logger.debug("Found %s tokens by user_id", len(models))
        return [self._to_entity(model) for model in models]

    def find_by_hashed_token(
        self,
        token_hash: HashedToken,
    ) -> RefreshTokenEntity | None:
        """Find a refresh token by hashed token

        Args:
            token_hash (HashedToken): hashed token to find

        Returns:
            RefreshTokenEntity | None: Return None, if none found
        """
        model = self._find_model_by_hashed_token(token_hash)
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
        stmt = delete(RefreshTokenModel).where(
            RefreshTokenModel.user_id == user_id.value
        )
        delete_count = self.session.execute(stmt).rowcount
        logger.info("Deleted %s tokens by user_id", delete_count)
        return delete_count

    def delete_by_hashed_token(self, token_hash: HashedToken) -> int:
        """Delete refresh token by hashed token

        Args:
            token_hash (HashedToken): hashed token to delete

        Returns:
            int: delete count
        """
        stmt = delete(RefreshTokenModel).where(
            RefreshTokenModel.token_hash == token_hash.value
        )
        delete_count = self.session.execute(stmt).rowcount
        logger.info("Deleted %s tokens by hashed token", delete_count)
        return delete_count

    def delete_expired_tokens(self, now: AwareDatetime) -> int:
        """Deletes all expired refresh tokens

        Returns:
            int: delete count
        """
        stmt = delete(RefreshTokenModel).where(
            RefreshTokenModel.expires_at <= now.value
        )
        delete_count = self.session.execute(stmt).rowcount
        logger.info("Deleted %s expired tokens", delete_count)
        return delete_count

    def delete_old_revoked_tokens(self, cutoff: AwareDatetime) -> int:
        """Deletes all old revoked tokens

        Returns:
            int: delete count
        """
        stmt = delete(RefreshTokenModel).where(
            RefreshTokenModel.revoked_at.isnot(None),
            RefreshTokenModel.revoked_at < cutoff.value,
        )
        delete_count = self.session.execute(stmt).rowcount
        logger.info("Deleted %s old revoked tokens", delete_count)
        return delete_count

    def _find_model_by_hashed_token(
        self,
        token_hash: HashedToken,
    ) -> RefreshTokenModel | None:
        """Find a SQLAlchemy model by hashed token

        Args:
            token_hash (HashedToken): Hashed token to find

        Returns:
            RefreshTokenModel | None: return none, if none found
        """
        stmt = select(RefreshTokenModel).where(
            RefreshTokenModel.token_hash == token_hash.value
        )
        return self.session.scalars(stmt).one_or_none()

    def _get_model_by_hashed_token_or_raise(
        self,
        token_hash: HashedToken,
    ) -> RefreshTokenModel:
        """Get a SQLAlchemy model by hashed token

        Args:
            token_hash (HashedToken): Hashed token to find

        Raises:
            TokenNotFoundError: if none found

        Returns:
            RefreshTokenModel: SQLAlchemy model
        """
        model = self._find_model_by_hashed_token(token_hash)
        if model is None:
            logger.warning("Token not found")
            raise TokenNotFoundError("Token not found")
        return model

    def _to_entity(self, model: RefreshTokenModel) -> RefreshTokenEntity:
        """SQLAlchemy model -> Domain entity"""
        return RefreshTokenEntity(
            id=RefreshTokenId(model.id),
            user_id=UserId(model.user_id),
            token_hash=HashedToken(model.token_hash),
            created_at=AwareDatetime(model.created_at),
            expires_at=AwareDatetime(model.expires_at),
            used_at=AwareDatetime(model.used_at) if model.used_at else None,
            revoked_at=AwareDatetime(model.revoked_at)
            if model.revoked_at
            else None,
        )

    def _to_model(self, entity: RefreshTokenEntity) -> RefreshTokenModel:
        """Domain entity -> SQLAlchemy model"""
        return RefreshTokenModel(
            id=entity.id.value,
            user_id=entity.user_id.value,
            token_hash=entity.token_hash.value,
            created_at=entity.created_at.value,
            expires_at=entity.expires_at.value,
            used_at=entity.used_at.value if entity.used_at else None,
            revoked_at=entity.revoked_at.value if entity.revoked_at else None,
        )
