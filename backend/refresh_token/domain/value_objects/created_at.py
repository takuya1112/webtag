from datetime import datetime

from shared.domain.exceptions import InvalidAwareDatetimeError
from shared.domain.value_objects import AwareDatetime

from ..exceptions import RefreshTokenCreatedAtInvalidError


class CreatedAt(AwareDatetime):
    def __init__(self, value: datetime):
        try:
            super().__init__(value)
        except InvalidAwareDatetimeError:
            raise RefreshTokenCreatedAtInvalidError() from None
