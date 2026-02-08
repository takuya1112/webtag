from .constants import ValidationLength

def _raise_if_value_empty(value: str, field_name: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} must be filled")
    return value

def validate_name(name: str) -> str:
    name = _raise_if_value_empty(name, "name")
    if len(name) > ValidationLength.USER_NAME_MAX:
        raise ValueError(
            f"name must be at most {ValidationLength.USER_NAME_MAX} characters."
        )
    return name

def validate_email(email: str) -> str:
    email = _raise_if_value_empty(email, "email")
    if len(email) > ValidationLength.USER_EMAIL_MAX:
        raise ValueError(
            f"email must be at most {ValidationLength.USER_EMAIL_MAX} characters."
        )
    return email

def validate_password(password: str) -> str:
    password = _raise_if_value_empty(password, "password")
    if len(password) < ValidationLength.USER_PASSWORD_MIN:
        raise ValueError(
            f"password must be at least {ValidationLength.USER_PASSWORD_MIN} characters."
        )
    if len(password) > ValidationLength.USER_PASSWORD_MAX:
        raise ValueError(
            f"password must be at most {ValidationLength.USER_PASSWORD_MAX} characters."
        )
    return password

def validate_title_required(title: str) -> str:
    title = _raise_if_value_empty(title, "title")
    if len(title) > ValidationLength.ARTICLE_TITLE_MAX:
        raise ValueError(
            f"title must be at most {ValidationLength.ARTICLE_TITLE_MAX} characters."
        )
    return title

def validate_title_optional(title: str | None) -> str | None:
    if title is None:
        return None
    else:
        return validate_title_required(title)