import pytest
from shared.domain.value_objects import AwareDatetime
from user.domain.entity import UserEntity
from user.domain.value_objects import Email, HashedPassword, UserName
from user.exceptions import UserAlreadyActive, UserAlreadyInactive


class TestIsActive:
    def test_active_when_deactivated_at_is_none(
        self,
        active_user: UserEntity,
    ):
        assert active_user.is_active is True

    def test_inactive_when_deactivated_at_is_set(
        self,
        inactive_user: UserEntity,
    ):
        assert inactive_user.is_active is False


class TestActivate:
    def test_activate_when_inactive(
        self,
        inactive_user: UserEntity,
        later: AwareDatetime,
    ):
        inactive_user.activate(later)
        assert inactive_user.is_active is True
        assert inactive_user.deactivated_at is None
        assert inactive_user.updated_at == later

    def test_activate_when_already_active(
        self,
        active_user: UserEntity,
        later: AwareDatetime,
    ):
        with pytest.raises(UserAlreadyActive):
            active_user.activate(later)


class TestDeactivate:
    def test_deactivate_when_active(
        self,
        active_user: UserEntity,
        later: AwareDatetime,
    ):
        active_user.deactivate(later)
        assert active_user.is_active is False
        assert active_user.deactivated_at == later
        assert active_user.updated_at == later

    def test_deactivate_when_already_inactive(
        self,
        inactive_user: UserEntity,
        later: AwareDatetime,
    ):
        with pytest.raises(UserAlreadyInactive):
            inactive_user.deactivate(later)


class TestChangeName:
    def test_change_name(
        self,
        active_user: UserEntity,
        later: AwareDatetime,
    ):
        new_name = UserName("new_name")
        active_user.change_name(new_name, later)
        assert active_user.name == new_name
        assert active_user.updated_at == later


class TestChangeEmail:
    def test_change_email(
        self,
        active_user: UserEntity,
        later: AwareDatetime,
    ):
        new_email = Email("new@example.com")
        active_user.change_email(new_email, later)
        assert active_user.email == new_email
        assert active_user.updated_at == later


class TestChangePassword:
    def test_change_password(
        self,
        active_user: UserEntity,
        later: AwareDatetime,
    ):
        new_password = HashedPassword("new_password")
        active_user.change_password(new_password, later)
        assert active_user.password_hash == new_password
        assert active_user.updated_at == later


class TestCanLogin:
    def test_active_user_can_login(self, active_user: UserEntity):
        assert active_user.can_login() is True

    def test_inactive_user_can_login(self, inactive_user: UserEntity):
        assert inactive_user.can_login() is False
