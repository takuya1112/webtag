from dataclasses import dataclass
from datetime import datetime

from shared.domain.value_objects import AppUuid, AwareDatetime

from ..exceptions import TokenAlreadyRevoked
from .value_objects import HashedToken


@dataclass
class RefreshTokenEntity:
    user_id: AppUuid
    hashed_token: HashedToken
    expires_at: AwareDatetime
    revoked_at: AwareDatetime | None = None

    def is_valid(self, current_time: datetime) -> bool:
        return not self.is_expired(current_time) and not self.is_revoked()

    def is_expired(self, current_time: datetime) -> bool:
        return self.expires_at <= current_time

    def is_revoked(self) -> bool:
        return self.revoked_at is not None

    def revoke(self, current_time: datetime) -> None:
        if self.is_revoked():
            raise TokenAlreadyRevoked()
        self.revoked_at = AwareDatetime(current_time)
