from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from ..models import User
from ..repositories import UserRepository
from ...schemas.user import UserCreate
from ...db.core import (
    EmailAlreadyExistsError, DatabaseConstraintError,
    UnexpectedError,
) 
from ..core.security import hash_password
from ...config.logging import get_logger

logger = get_logger(__name__)

class UserService:
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
            if isinstance(e.orig, UniqueViolation) and "email" in str(e.orig):
                logger.error(f"エラーです {e.orig}")
                raise EmailAlreadyExistsError()
            
            raise DatabaseConstraintError(f": {str(e)}")
