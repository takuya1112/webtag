from typing import Annotated
from pydantic import AfterValidator
from core.validators import (
    validate_name, validate_email, validate_password,
    validate_title_required, validate_title_optional
)

ValidateName = Annotated [str, AfterValidator(validate_name)]
ValidateEmail = Annotated[str, AfterValidator(validate_email)]
ValidatePassword = Annotated[str, AfterValidator(validate_password)]

ValidateTitleRequired = Annotated[str, AfterValidator(validate_title_required)]
ValidateTitleOptional = Annotated[str | None, AfterValidator(validate_title_optional)]