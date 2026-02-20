from datetime import datetime, timezone
from uuid import UUID

from shared.domain.value_objects import AwareDatetime
from user.domain.entity import UserEntity


class TestUserFactory:
    def test_create_return_entity(self, created_user: UserEntity):
        assert isinstance(created_user, UserEntity)

    def test_name_is_set(self, created_user: UserEntity):
        assert created_user.name.value == "test_user"

    def test_email_is_set(self, created_user: UserEntity):
        assert created_user.email.value == "test@example.com"

    def test_password_hash_is_set(self, created_user: UserEntity):
        assert created_user.password_hash.value == "hashed_password"

    def test_id_is_set(self, created_user: UserEntity):
        assert created_user.id.value == UUID(
            "01900000-0000-7000-8000-000000000001",
        )

    def test_created_at_is_set(self, created_user: UserEntity):
        expected = AwareDatetime(datetime(2026, 1, 1, tzinfo=timezone.utc))
        assert created_user.created_at == expected

    def test_updated_at_is_set(self, created_user: UserEntity):
        expected = AwareDatetime(datetime(2026, 1, 1, tzinfo=timezone.utc))
        assert created_user.updated_at == expected

    def test_updated_at_equal_created_at(self, created_user: UserEntity):
        assert created_user.created_at == created_user.updated_at

    def test_deactivated_at_is_none(self, created_user: UserEntity):
        assert created_user.deactivated_at is None

    def test_is_active_on_creation(self, created_user: UserEntity):
        assert created_user.is_active is True
