from dataclasses import dataclass

from core.constants import UserConfig

from ..exceptions import UserNameEmptyError, UserNameTooLongError


@dataclass(frozen=True)
class UserName:
    """User name value object

    Raises:
        UserNameEmptyError: raise if user name is empty
        UserNameTooLongError: raise if user name is too long
    """

    value: str

    def __post_init__(self):
        object.__setattr__(self, "value", self.value.strip())

        if not self.value:
            raise UserNameEmptyError()

        if len(self.value) > UserConfig.NAME_LENGTH_MAX:
            raise UserNameTooLongError(
                max_length=UserConfig.NAME_LENGTH_MAX,
            )

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"UserName('{self.value}')"
