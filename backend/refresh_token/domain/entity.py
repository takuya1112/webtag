from dataclasses import dataclass

from user.domain.value_objects import UserId

from .exceptions import (
    RefreshTokenAlreadyRevokedError,
    RefreshTokenAlreadyUsedError,
    RefreshTokenExpiredError,
)
from .value_objects import (
    CreatedAt,
    ExpiredAt,
    RefreshTokenHash,
    RefreshTokenId,
    RevokedAt,
    UsedAt,
)


@dataclass
class RefreshTokenEntity:
    id: RefreshTokenId
    user_id: UserId
    token_hash: RefreshTokenHash
    created_at: CreatedAt
    expires_at: ExpiredAt
    used_at: UsedAt | None = None
    revoked_at: RevokedAt | None = None

    def ensure_useable(self, expires_at: ExpiredAt) -> None:
        if self.is_expired(expires_at):
            raise RefreshTokenExpiredError()
        if self.is_used():
            raise RefreshTokenAlreadyUsedError()
        if self.is_revoked():
            raise RefreshTokenAlreadyRevokedError()

    def is_expired(self, expires_at: ExpiredAt) -> bool:
        return self.expires_at <= expires_at

    def is_used(self) -> bool:
        return self.used_at is not None

    def is_revoked(self) -> bool:
        return self.revoked_at is not None

    def mark_used(self, used_at: UsedAt) -> None:
        if self.is_used():
            raise RefreshTokenAlreadyUsedError()
        self.used_at = used_at

    def revoke(self, revoked_at: RevokedAt) -> None:
        if self.is_revoked():
            raise RefreshTokenAlreadyRevokedError()
        self.revoked_at = revoked_at
