from dataclasses import dataclass

from shared.domain.value_objects import AwareDatetime
from user.domain.value_objects import UserId

from ..exceptions import TokenAlreadyRevoked
from .value_objects import HashedToken


@dataclass
class RefreshTokenEntity:
    user_id: UserId
    token_hash: HashedToken
    expires_at: AwareDatetime
    revoked_at: AwareDatetime | None = None

    def is_valid(self, now: AwareDatetime) -> bool:
        return not self.is_expired(now) and not self.is_revoked()

    def is_expired(self, now: AwareDatetime) -> bool:
        return self.expires_at <= now

    def is_revoked(self) -> bool:
        return self.revoked_at is not None

    def revoke(self, now: AwareDatetime) -> None:
        if self.is_revoked():
            raise TokenAlreadyRevoked()
        self.revoked_at = AwareDatetime(now)
