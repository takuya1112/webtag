from datetime import datetime, timezone
from uuid import UUID

import pytest
from shared.domain.value_objects import AppUuid, AwareDatetime


class TestAppUuid:
    def test_valid_uuid(self):
        uid = AppUuid(UUID("01900000-0000-7000-8000-000000000001"))
        assert isinstance(uid.value, UUID)

    def test_invalid_uuid(self):
        with pytest.raises(ValueError):
            AppUuid("not-uuid")


class TestAwareDatetime:
    def test_valid_aware_datetime(self):
        dt = AwareDatetime(datetime(2026, 1, 1, tzinfo=timezone.utc))
        assert dt.value.tzinfo is not None

    def test_invalid_naive_datetime_raises(self):
        with pytest.raises(ValueError):
            AwareDatetime(datetime(2026, 1, 1))

    def test_comparison_le(self, now: AwareDatetime, later: AwareDatetime):
        assert now <= later.value
        assert now <= later

    def test_comparison_it(self, now: AwareDatetime, later: AwareDatetime):
        assert now < later.value
        assert now < later

    def test_comparison_ge(self, now: AwareDatetime, later: AwareDatetime):
        assert later.value >= now
        assert later >= now

    def test_comparison_gt(self, now: AwareDatetime, later: AwareDatetime):
        assert later.value > now
        assert later > now

    def test_comparison_ep(self, now: AwareDatetime):
        assert now == now.value
        assert now == now
