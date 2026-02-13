from typing import Annotated
from pydantic import StringConstraints
from core.constants import TagConfig


ValidNameRequired = Annotated[
    str,
    StringConstraints(
        min_length=TagConfig.NAME_LENGTH_MIN,
        max_length=TagConfig.NAME_LENGTH_MAX,
        strip_whitespace=True,
    )
]