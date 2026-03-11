from typing import Annotated

from core.constants import UserConfig
from pydantic import (
    StringConstraints,
)

ValidateNameRequired = Annotated[
    str,
    StringConstraints(
        min_length=UserConfig.NAME_LENGTH_MIN,
        max_length=UserConfig.NAME_LENGTH_MAX,
        strip_whitespace=True,
    ),
]


ValidatePasswordRequired = Annotated[
    str,
    StringConstraints(
        min_length=UserConfig.PASSWORD_LENGTH_MIN,
        max_length=UserConfig.PASSWORD_LENGTH_MAX,
    ),
]
