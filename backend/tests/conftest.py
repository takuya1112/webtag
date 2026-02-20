from datetime import datetime, timedelta, timezone

import pytest
from shared.domain.value_objects import AwareDatetime


@pytest.fixture
def now():
    return AwareDatetime(datetime(2026, 1, 1, tzinfo=timezone.utc))


@pytest.fixture
def later(now: AwareDatetime):
    return AwareDatetime(now.value + timedelta(hours=1))
