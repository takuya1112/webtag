from core.constants import UserConfig
from shared.infrastructure.base import Base
from sqlalchemy import Column, DateTime, Index, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class UserModel(Base):
    """User Model"""

    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True)
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
        "ArticleModel",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    tags = relationship(
        "TagModel",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    refresh_tokens = relationship(
        "RefreshTokenModel",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index(
            "ix_users_active",
            id,
            postgresql_where=(deactivated_at.is_(None)),
        ),
    )
