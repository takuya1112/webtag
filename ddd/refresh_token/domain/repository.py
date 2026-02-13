from typing import Protocol

from .entity import RefreshTokenEntity
from .value_objects import HashedToken, UserId


class RefreshTokenRepository(Protocol):
    """Refresh token repository interface"""

    def save(self, token: RefreshTokenEntity) -> None:
        """Persist a refresh token

        Args:
            token (RefreshTokenEntity): The refresh token to persist
        """
        ...

    def find_by_user_id(self, user_id: UserId) -> list[RefreshTokenEntity]:
        """Find all refresh tokens by user id

        Args:
            user_id (UserId): user id

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
            hashed_token (HashedToken): hashed token

        Returns:
            RefreshTokenEntity | None: Return None, if none found
        """
        ...

    def delete_all_by_user_id(self, user_id: UserId) -> None:
        """Delete all refresh tokens by user id

        Args:
            user_id (UserId): user id
        """
        ...

    def delete_by_hashed_token(self, hashed_token: HashedToken) -> None:
        """Delete refresh token by hashed token

        Args:
            hashed_token (HashedToken): hashed token to delete
        """
        ...

    def delete_expired_tokens(self) -> None:
        """Deletes all expired refresh tokens"""
        ...
