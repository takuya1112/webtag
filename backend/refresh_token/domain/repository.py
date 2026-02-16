from typing import Protocol

from shared.domain.value_objects import UserId

from .entity import RefreshTokenEntity
from .value_objects import HashedToken


class RefreshTokenRepository(Protocol):
    """Refresh token repository interface"""

    def add(self, token: RefreshTokenEntity) -> None:
        """Add a refresh token

        Args:
            token (RefreshTokenEntity): The refresh token to add
        """
        ...

    def update(self, token: RefreshTokenEntity) -> None:
        """Update a refresh token

        Args:
            token (RefreshTokenEntity): The refresh token to update

        Raises:
            TokenNotFoundError: if none found
        """
        ...

    def find_by_user_id(self, user_id: UserId) -> list[RefreshTokenEntity]:
        """Find all refresh tokens by user id

        Args:
            user_id (UserId): user id to find

        Returns:
            list[RefreshTokenEntity]: Return empty list, if none found
        """
        ...

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
        ...

    def delete_all_by_user_id(self, user_id: UserId) -> int:
        """Delete all refresh tokens by user id

        Args:
            user_id (UserId): user id

        Returns:
            int: delete count
        """
        ...

    def delete_by_hashed_token(self, hashed_token: HashedToken) -> int:
        """Delete refresh token by hashed token

        Args:
            hashed_token (HashedToken): hashed token to delete

        Returns:
            int: delete count
        """
        ...

    def delete_expired_tokens(self) -> int:
        """Deletes all expired refresh tokens

        Returns:
            int: delete count
        """
        ...

    def delete_old_revoked_tokens(self) -> int:
        """Deletes all old revoked tokens

        Returns:
            int: delete count
        """
        ...
