import re
from dataclasses import dataclass

from core.constants import UserConfig

from ..exceptions import InvalidEmailError

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self):
        if not self.value:
            raise InvalidEmailError("Email must be filled")

        if len(self.value) > UserConfig.DB_EMAIL_LENGTH_MAX:
            raise InvalidEmailError("Email is too long")

        if not EMAIL_REGEX.match(self.value):
            raise InvalidEmailError("Invalid email")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"Email('{self.value}')"

    @property
    def domain(self) -> str:
        return self.value.split("@")[1]

    @property
    def local_part(self) -> str:
        return self.value.split("@")[0]
