import pytest
from tests.unit.shared.fakes import FakeUnitOfWork
from tests.unit.user.fakes import FakeUserRepository
from user.application.create import CreateUser
from user.exceptions import EmailAlreadyExistError


class TestCreateUser:
    def test_valid_case(
        self,
        fake_create_user: CreateUser,
        fake_user_repository: FakeUserRepository,
        fake_user_uow: FakeUnitOfWork,
    ):
        result = fake_create_user.execute(
            name="test_user",
            email="test@example.com",
            password="password",
        )

        assert result is not None
        assert len(fake_user_repository.store) == 1
        assert fake_user_uow.committed is True

    def test_email_already_exist(self, fake_create_user: CreateUser):
        fake_create_user.execute(
            name="test_user",
            email="test@example.com",
            password="password",
        )

        with pytest.raises(EmailAlreadyExistError):
            fake_create_user.execute(
                name="test_user",
                email="test@example.com",
                password="password",
            )
