from sqlalchemy import (
    Column, BigInteger, String, Boolean, DateTime, 
    text, func 
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from ..core import Base


class User(Base):
    """User Model

    Attributes:
        id: The Primary Key of the user.
        name: The name of the user.
        email:
    """

    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    public_id = Column(UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)
    name = Column(String(300), nullable=False)
    email = Column(String(300), unique=True, nullable=False)
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
    deactivated_at = Column(DateTime(timezone=True))

    articles = relationship("Article", back_populates="users")
    tags = relationship("Tag", back_populates="users")