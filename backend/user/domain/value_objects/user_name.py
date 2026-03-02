from dataclasses import dataclass

from core.constants import UserConfig

from ..exceptions import InvalidUserNameError


@dataclass(frozen=True)
class UserName:
    """User name value object

    Raises:
        InvalidUserNameError: raise if user name is empty
        InvalidUserNameError: raise if user name is too long
    """

    value: str

    def __post_init__(self):
        object.__setattr__(self, "value", self.value.strip())

        if not self.value:
            raise InvalidUserNameError("UserName must be filled")

        if len(self.value) > UserConfig.NAME_LENGTH_MAX:
            raise InvalidUserNameError("UserName is too long")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"UserName('{self.value}')"
