import pytest
from tests.unit.shared.fakes import FakeClock, FakeIdGenerator


@pytest.fixture
def fake_clock() -> FakeClock:
    return FakeClock()


@pytest.fixture
def fake_id_generator() -> FakeIdGenerator:
    return FakeIdGenerator()
