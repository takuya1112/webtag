from typing import Annotated
from pydantic import StringConstraints, HttpUrl
from core.constants import ArticleConfig


ValidateTitleRequired = Annotated[
    str, 
    StringConstraints(
        min_length=ArticleConfig.TITLE_LENGTH_MIN,
        max_length=ArticleConfig.TITLE_LENGTH_MAX,
        strip_whitespace=True,
    )
]

ValidateTitleOptional = Annotated[
    str | None, 
    StringConstraints(
        min_length=ArticleConfig.TITLE_LENGTH_MIN,
        max_length=ArticleConfig.TITLE_LENGTH_MAX, 
        strip_whitespace=True
    )
]

ValidateUrlRequired = HttpUrl

ValidateUrlOptional= HttpUrl | None