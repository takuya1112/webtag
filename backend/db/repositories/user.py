from sqlalchemy.orm import Session
from ..models import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: User) -> None:
        self.session.add(user)
        self.session.flush()