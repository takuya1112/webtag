from sqlalchemy import (
    Column, BigInteger, String, Boolean, DateTime, 
    text, func 
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from ..session import Base
from core.constants import UserConfig


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
    name = Column(String(UserConfig.DB_NAME_LENGTH_MAX), nullable=False)
    email = Column(String(UserConfig.DB_EMAIL_LENGTH_MAX), unique=True, nullable=False)
    password_hash = Column(String(UserConfig.DB_PASSWORD_LENGTH_MAX), nullable=False)
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

    articles = relationship("Article", back_populates="user")
    tags = relationship("Tag", back_populates="user")