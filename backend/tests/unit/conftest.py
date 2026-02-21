import pytest
from tests.unit.shared.fakes import (
    FakeClock,
    FakeIdGenerator,
    FakePasswordHasher,
)


@pytest.fixture
def fake_clock() -> FakeClock:
    return FakeClock()


@pytest.fixture
def fake_id_generator() -> FakeIdGenerator:
    return FakeIdGenerator()


@pytest.fixture
def fake_password_hasher() -> FakePasswordHasher:
    return FakePasswordHasher()
