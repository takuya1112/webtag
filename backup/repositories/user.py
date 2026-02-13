from sqlalchemy.orm import Session
from db.models import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_public_id(self, public_id: int) -> User | None:
        return (
            self.session
            .query(User)
            .filter(User.public_id == public_id)
            .one_or_none()
        )

    def get_by_email(self, email: str) -> User | None:
        return (
            self.session
            .query(User)
            .filter(User.email == email)
            .one_or_none()
        )

    def add(self, user: User) -> None:
        self.session.add(user)
        self.session.flush()

    def update_hash(self, user: User, new_hash: str) -> None:
        user.password_hash = new_hash
        self.session.flush()