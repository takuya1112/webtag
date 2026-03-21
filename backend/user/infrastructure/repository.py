from core.logging import get_logger
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..domain.entity import UserEntity
from ..domain.value_objects import (
    CreatedAt,
    DeactivatedAt,
    Email,
    HashedPassword,
    UpdatedAt,
    UserId,
    UserName,
)
from .exceptions import UserNotFoundError
from .model import UserModel

logger = get_logger(__name__)


class SQLAlchemyUserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: UserEntity) -> None:
        """Add a user

        Args:
            user (UserEntity): The user to add
        """
        model = self._to_model(user)
        self.session.add(model)
        logger.debug("User added: user_id=%s", user.id.value)

    def update(self, user: UserEntity) -> None:
        """Update a user

        Args:
            user (UserEntity): The user to update

        Raises:
            UserNotFoundError: if none found
        """
        model = self._get_model_by_id_or_raise(user.id)
        model.name = user.name.value
        model.email = user.email.value
        model.password_hash = user.password_hash.value
        model.updated_at = user.updated_at.value
        model.deactivated_at = (
            user.deactivated_at.value if user.deactivated_at else None
        )
        logger.debug("User updated: user_id=%s", user.id.value)

    def find_by_id(self, user_id: UserId) -> UserEntity | None:
        """Find a user by user id

        Args:
            user_id (UserId): The user id to find

        Returns:
            UserEntity | None: Return none, if none found
        """
        model = self._find_model_by_id(user_id)
        if model:
            logger.debug("User found by user id: %s", user_id.value)
        else:
            logger.debug("User not found by user id: %s", user_id.value)
        return self._to_entity(model) if model else None

    def find_by_email(self, email: Email) -> UserEntity | None:
        """Find a user by email

        Args:
            email (Email): Email to find

        Returns:
            UserEntity | None: Return none, if none found
        """
        stmt = select(UserModel).where(UserModel.email == email.value)
        model = self.session.scalars(stmt).one_or_none()
        if model:
            logger.debug("User found by email")
        else:
            logger.debug("User not found by email")
        return self._to_entity(model) if model else None

    def _find_model_by_id(self, user_id: UserId) -> UserModel | None:
        """Find a user model by user id

        Args:
            user_id (UserId): The user id to find

        Returns:
            UserModel: Return none, if none found
        """
        return self.session.get(UserModel, user_id.value)

    def _get_model_by_id_or_raise(
        self,
        user_id: UserId,
    ) -> UserModel:
        """Get a user model by user id

        Args:
            user_id (UserId): The user id to find

        Raises:
            UserNotFoundError: if none found

        Returns:
            UserModel: SQLAlchemy model
        """
        model = self._find_model_by_id(user_id)
        if model is None:
            logger.warning("User not found by user id: %s", user_id.value)
            raise UserNotFoundError()
        return model

    def _to_entity(self, model: UserModel) -> UserEntity:
        """SQLAlchemy model -> Domain entity"""
        return UserEntity(
            id=UserId(model.id),
            name=UserName(model.name),
            email=Email(model.email),
            password_hash=HashedPassword(model.password_hash),
            created_at=CreatedAt(model.created_at),
            updated_at=UpdatedAt(model.updated_at),
            deactivated_at=DeactivatedAt(model.deactivated_at)
            if model.deactivated_at
            else None,
        )

    def _to_model(self, entity: UserEntity) -> UserModel:
        """Domain entity -> SQLAlchemy model"""
        return UserModel(
            id=entity.id.value,
            name=entity.name.value,
            email=entity.email.value,
            password_hash=entity.password_hash.value,
            created_at=entity.created_at.value,
            updated_at=entity.updated_at.value,
            deactivated_at=entity.deactivated_at.value
            if entity.deactivated_at
            else None,
        )
