from dataclasses import dataclass

from shared.domain.value_objects import AwareDatetime
from user.domain.value_objects import UserId

from ..exceptions import TokenAlreadyRevoked, TokenAlreadyUsed
from .value_objects import HashedToken, RefreshTokenId


@dataclass
class RefreshTokenEntity:
    id: RefreshTokenId
    user_id: UserId
    token_hash: HashedToken
    created_at: AwareDatetime
    expires_at: AwareDatetime
    used_at: AwareDatetime | None = None
    revoked_at: AwareDatetime | None = None

    def is_valid(self, now: AwareDatetime) -> bool:
        return (
            not self.is_expired(now)
            and not self.is_used()
            and not self.is_revoked()
        )

    def is_expired(self, now: AwareDatetime) -> bool:
        return self.expires_at <= now

    def is_used(self) -> bool:
        return self.used_at is not None

    def is_revoked(self) -> bool:
        return self.revoked_at is not None

    def mark_used(self, now: AwareDatetime) -> None:
        if self.is_used():
            raise TokenAlreadyUsed()
        self.used_at = now

    def revoke(self, now: AwareDatetime) -> None:
        if self.is_revoked():
            raise TokenAlreadyRevoked()
        self.revoked_at = now
