from sqlalchemy.orm import Session
from ..models import User
from ..repositories import UserRepository
from ...schemas.user import UserCreate
from ..core.security import hash_password
from sqlalchemy.exc import IntegrityError
from ...schemas import EmailAlreadyExistsError

class UserService:
    def __init__(self, session: Session):
        self.repo = UserRepository(session)

    def create(self, create_data: UserCreate) -> User:
        if self.repo.get_by_email(create_data.email):
            raise EmailAlreadyExistsError()

        user = User(
            name=create_data.name,
            email=create_data.email,
            password_hash=hash_password(create_data.password) 
        )