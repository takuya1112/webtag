from core.constants import UserConfig
from shared.infrastructure.base import Base
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class UserModel(Base):
    """User Model

    Attributes:
        id: The Primary Key of the user.
        name: The name of the user.
        email:
    """

    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    public_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
    name = Column(String(UserConfig.DB_NAME_LENGTH_MAX), nullable=False)
    email = Column(
        String(UserConfig.DB_EMAIL_LENGTH_MAX),
        unique=True,
        nullable=False,
    )
    password_hash = Column(
        String(UserConfig.DB_PASSWORD_LENGTH_MAX),
        nullable=False,
    )
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
    deactivated_at = Column(DateTime(timezone=True), nullable=True)

    articles = relationship(
        "Article",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    tags = relationship(
        "Tag",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    refresh_tokens = relationship(
        "RefreshToken",
        back_populates="user",
        cascade="all, delete-orphan",
    )
