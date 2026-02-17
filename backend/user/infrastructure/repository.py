from core.logging import get_logger
from shared.domain.value_objects.aware_datetime import AwareDatetime
from sqlalchemy.orm import Session

from ..domain.entity import UserEntity
from ..domain.value_objects import Email, HashedPassword, UserId, UserName
from ..exceptions import UserNotFoundError
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
        logger.info("User added")

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

    def find_by_id(self, user_id: UserId) -> UserEntity | None:
        """Find a user by user id

        Args:
            user_id (UserId): The user id to find

        Returns:
            UserEntity | None: Return none, if none found
        """
        model = self.session.get(UserModel, user_id.value)
        if model:
            logger.debug("User found by user id: %s", str(user_id.value))
        else:
            logger.debug("User not found by user id: %s", str(user_id.value))
        return self._to_entity(model) if model else None

    def find_by_email(self, email: Email) -> UserEntity | None:
        """Find a user by email

        Args:
            email (Email): Email to find

        Returns:
            UserEntity | None: Return none, if none found
        """
        model = (
            self.session.query(UserModel)
            .filter(UserModel.email == email.value)
            .one_or_none()
        )
        if model:
            logger.debug("User found by email")
        else:
            logger.debug("User not found by email")
        return self._to_entity(model) if model else None

    def _get_model_by_id_or_raise(
        self,
        user_id: UserId,
    ) -> UserModel:
        """Get a user model by user id

        Args:
            user_id (UserId): user id to find

        Raises:
            UserNotFoundError: if none found

        Returns:
            UserModel: SQLAlchemy model
        """
        model = self.session.get(UserModel, user_id.value)
        if model is None:
            logger.warning("User not found by user id: %s", str(user_id.value))
            raise UserNotFoundError("User not found")
        return model

    def _to_entity(self, model: UserModel) -> UserEntity:
        """SQLAlchemy model -> Domain entity"""
        return UserEntity(
            id=UserId(model.id),
            name=UserName(model.name),
            email=Email(model.email),
            password_hash=HashedPassword(model.password_hash),
            created_at=AwareDatetime(model.created_at),
            updated_at=AwareDatetime(model.updated_at),
            deactivated_at=AwareDatetime(model.deactivated_at)
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
