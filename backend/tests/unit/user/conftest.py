from uuid import UUID

import pytest
from shared.domain.value_objects import AwareDatetime
from tests.unit.user.fakes import FakeUserRepository
from user.domain.entity import UserEntity
from user.domain.factory import UserFactory
from user.domain.value_objects import Email, HashedPassword, UserId, UserName


@pytest.fixture
def active_user(now: AwareDatetime) -> UserEntity:
    return UserEntity(
        id=UserId(UUID("01900000-0000-7000-8000-000000000001")),
        name=UserName("test_user"),
        email=Email("test@example.com"),
        password_hash=HashedPassword("hashed_password"),
        created_at=now,
        updated_at=now,
        deactivated_at=None,
    )


@pytest.fixture
def inactive_user(now: AwareDatetime) -> UserEntity:
    return UserEntity(
        id=UserId(UUID("01900000-0000-7000-8000-000000000001")),
        name=UserName("test_user"),
        email=Email("test@example.com"),
        password_hash=HashedPassword("hashed_password"),
        created_at=now,
        updated_at=now,
        deactivated_at=now,
    )


@pytest.fixture
def fake_user_factory(fake_id_generator, fake_clock) -> UserFactory:
    return UserFactory(
        generator=fake_id_generator,
        clock=fake_clock,
    )


@pytest.fixture
def created_user(fake_user_factory: UserFactory) -> UserEntity:
    return fake_user_factory.create(
        name=UserName("test_user"),
        email=Email("test@example.com"),
        password_hash=HashedPassword("hashed_password"),
    )


@pytest.fixture
def fake_user_repository() -> FakeUserRepository:
    return FakeUserRepository()
