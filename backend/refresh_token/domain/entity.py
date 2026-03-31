from dataclasses import dataclass

from shared.domain.value_objects import AwareDatetime
from user.domain.value_objects import UserId

from .exceptions import (
    ExpiredRefreshTokenError,
    RefreshTokenAlreadyRevoked,
    RefreshTokenAlreadyUsed,
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

    def ensure_useable(self, now: AwareDatetime) -> None:
        if self.is_expired(now):
            raise ExpiredRefreshTokenError()
        if self.is_used():
            raise RefreshTokenAlreadyUsed()
        if self.is_revoked():
            raise RefreshTokenAlreadyRevoked()

    def is_expired(self, now: AwareDatetime) -> bool:
        return self.expires_at <= now

    def is_used(self) -> bool:
        return self.used_at is not None

    def is_revoked(self) -> bool:
        return self.revoked_at is not None

    def mark_used(self, now: AwareDatetime) -> None:
        if self.is_used():
            raise RefreshTokenAlreadyUsed()
        self.used_at = now

    def revoke(self, now: AwareDatetime) -> None:
        if self.is_revoked():
            raise RefreshTokenAlreadyRevoked()
        self.revoked_at = now
