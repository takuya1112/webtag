from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from db.models import User
from repositories import UserRepository
from schemas.user import UserCreate
from core import (
    hash_password, get_logger,
    EmailAlreadyExistsError, UnexpectedError,
) 


logger = get_logger(__name__)

class UserService:
    CONSTRAINT_NAMES = {
        "USER_EMAIL_UNIQUE": "users_email_key"
    }

    def __init__(self, session: Session):
        self.repo = UserRepository(session)

    def create(self, create_data: UserCreate) -> User:
        user = User(
            name=create_data.name,
            email=create_data.email,
            password_hash=hash_password(create_data.password), 
        )
        try:
            self.repo.add(user)
            return user
        except IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):
                constraint_name = e.orig.diag.constraint_name
                if constraint_name == self.CONSTRAINT_NAMES["USER_EMAIL_UNIQUE"]:
                    logger.warning(f"Email already exist: {e.orig}")
                    raise EmailAlreadyExistsError()
            logger.error(f"Unexpected error happened: {e.orig}")
            raise UnexpectedError(f"Failed to create user") from e
