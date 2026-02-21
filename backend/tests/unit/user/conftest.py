from uuid import UUID

import pytest
from shared.domain.value_objects import AwareDatetime
from tests.unit.shared.fakes import FakePasswordHasher, FakeUnitOfWork
from tests.unit.user.fakes import FakeUserRepository
from user.application.create import CreateUser
from user.domain.entity import UserEntity
from user.domain.factory import UserFactory
from user.domain.value_objects import Email, HashedPassword, UserId, UserName
from user.infrastructure.repository import SQLAlchemyUserRepository


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


@pytest.fixture
def fake_user_uow(fake_user_repository: FakeUserRepository) -> FakeUnitOfWork:
    return FakeUnitOfWork(
        repositories={
            SQLAlchemyUserRepository: fake_user_repository,
        }
    )


@pytest.fixture
def fake_create_user(
    fake_user_uow: FakeUnitOfWork,
    fake_user_factory: UserFactory,
    fake_password_hasher: FakePasswordHasher,
) -> CreateUser:
    return CreateUser(
        uow=fake_user_uow,
        repository=SQLAlchemyUserRepository,
        factory=fake_user_factory,
        password_hasher=fake_password_hasher,
    )
