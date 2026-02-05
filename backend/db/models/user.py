from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, 
    text, func 
)
from sqlalchemy.orm import relationship
from ..core import Base


class User(Base):
    """User Model

    Attributes:
        id: The Primary Key of the user.
        name: The name of the user.
        email:
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), nullable=False)
    email = Column(String(300), nullable=False, unique=True)
    password_hash = Column(String(300), nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
    is_active = Column(Boolean, server_default=text("false"), nullable=False)

    articles = relationship("Article", back_populates="users")
    tags = relationship("Tag", back_populates="users")

    def __repr__(self) -> str:
        return f"<User(id = {self.id}, name = {self.name})>"