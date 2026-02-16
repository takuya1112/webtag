from datetime import UTC, datetime

from ..domain.clock import Clock
from ..domain.value_objects import AwareDatetime


class SystemClock(Clock):
    def now(self) -> AwareDatetime:
        return AwareDatetime(datetime.now(UTC))
