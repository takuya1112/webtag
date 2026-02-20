import pytest
from user.domain.value_objects import Email, HashedPassword, UserName

USER_NAME_TEST_MAX = 100
EMAIL_TEST_MAX = 500
HASHED_PASSWORD_TEST_MAX = 1000


class TestUserName:
    def test_valid_name(self):
        name = UserName("test")
        assert name.value == "test"

    def test_stripes_whitespace(self):
        name = UserName("             test                ")
        assert name.value == "test"

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            UserName("")

    def test_whitespace_only_raises(self):
        with pytest.raises(ValueError):
            UserName("                ")

    def test_too_long_raises(self):
        with pytest.raises(ValueError):
            UserName("a" * USER_NAME_TEST_MAX)


class TestEmail:
    def test_valid_email(self):
        email = Email("test@example.com")
        assert email.value == "test@example.com"

    def test_invalid_email(self):
        with pytest.raises(ValueError):
            Email("invalid-email")

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            Email("")

    def test_too_long_raises(self):
        long_email = "a" * EMAIL_TEST_MAX + "@example.com"
        with pytest.raises(ValueError):
            Email(long_email)

    def test_no_at_raises(self):
        with pytest.raises(ValueError):
            Email("testexample.com")

    def test_domain_property(self):
        email = Email("test@example.com")
        assert email.domain == "example.com"

    def test_local_part_property(self):
        email = Email("test@example.com")
        assert email.local_part == "test"


class TestHashedPassword:
    def test_valid_password(self):
        pwd = HashedPassword("hashed_password")
        assert pwd.value == "hashed_password"

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            HashedPassword("")

    def test_too_long_raises(self):
        with pytest.raises(ValueError):
            HashedPassword("a" * HASHED_PASSWORD_TEST_MAX)

    def test_str_returns_masked(self):
        pwd = HashedPassword("hashed_password")
        assert str(pwd) == "***HASHED***"

    def test_repr_returns_masked(self):
        pwd = HashedPassword("hashed_password")
        assert "***" in repr(pwd)
