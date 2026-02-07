from sqlalchemy.orm import Session
from ..models import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_email(self, email: str) -> User | None:
        return (
            self.session.query(User)
            .filter(User.email == email)
            .first()
        )

    def add(self, user: User) -> None:
        self.session.add(user)
        self.session.flush()