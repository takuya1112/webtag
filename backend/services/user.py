from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from db.models import User
from repositories import UserRepository
from schemas.user import UserCreate
from schemas.auth import LoginRequest
from core import (
    hash_password, get_logger,
    verify_and_update_password,
    EmailAlreadyExistsError, UnexpectedError,
    EmailPasswordWrongError,
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
    
    def authenticate(self, data: LoginRequest) -> User:
        user = self.repo.get_by_email(data.email)
        if not user:
            raise EmailPasswordWrongError()
        verified, new_hash = verify_and_update_password(
            password=data.password,
            hashed_password=user.password_hash,
        )

        if not verified:
            raise EmailPasswordWrongError()
        
        if new_hash:
            self.repo.update_hash(user, new_hash)

        return user
