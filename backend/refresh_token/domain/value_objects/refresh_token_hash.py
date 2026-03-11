from dataclasses import dataclass

from ..exceptions import RefreshTokenHashEmptyError


@dataclass(frozen=True)
class RefreshTokenHash:
    """Hashed refresh token value object

    Raises:
        RefreshTokenEmptyError: raise if hashed token is empty
    """

    value: str

    def __post_init__(self):
        if not self.value:
            raise RefreshTokenHashEmptyError()

    def __str__(self):
        return self.value
