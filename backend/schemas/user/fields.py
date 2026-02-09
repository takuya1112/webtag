from typing import Annotated
from pydantic import StringConstraints, EmailStr
from core.constants import UserConfig


ValidateNameRequired = Annotated[
    str,
    StringConstraints(
        min_length=UserConfig.NAME_LENGTH_MIN,
        max_length=UserConfig.NAME_LENGTH_MAX,
        strip_whitespace=True,
    ),         
]

ValidateEmailRequired = EmailStr

ValidatePasswordRequired = Annotated[
    str, 
    StringConstraints(
        min_length=UserConfig.PASSWORD_LENGTH_MIN,
        max_length=UserConfig.PASSWORD_LENGTH_MAX,
        strip_whitespace=True,
    ),
]