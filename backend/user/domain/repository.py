from typing import Protocol, runtime_checkable

from .entity import UserEntity
from .value_objects import UserEmail, UserId


@runtime_checkable
class UserRepository(Protocol):
    """User repository interface"""

    def add(self, user: UserEntity) -> None:
        """Add a user

        Args:
            user (UserEntity): The user to add
        """
        ...

    def update(self, user: UserEntity) -> None:
        """Update a user

        Args:
            user (UserEntity): The user to update

        Raises:
            UserNotFoundError: if none found
        """
        ...

    def find_by_id(self, user_id: UserId) -> UserEntity | None:
        """Find a user by user id

        Args:
            user_id (UserId): The user id to find

        Returns:
            UserEntity | None: Return none, if none found
        """
        ...

    def find_by_email(self, email: UserEmail) -> UserEntity | None:
        """Find a user by email

        Args:
            email (UserEmail): Email to find

        Returns:
            UserEntity | None: Return none, if none found
        """
        ...
