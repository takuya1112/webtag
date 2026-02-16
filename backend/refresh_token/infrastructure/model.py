from core.constants import RefreshTokenConfig
from shared.infrastructure.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class RefreshTokenModel(Base):
    """RefreshToken Model"""

    __tablename__ = "refresh_tokens"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    token_hash = Column(
        String(RefreshTokenConfig.DB_REFRESH_TOKEN_LENGTH_MAX),
        unique=True,
        nullable=False,
    )
    created_at = Column(DateTime(timezone=True), nullable=False)
    expires_at = Column(DateTime(timezone=True), index=True, nullable=False)
    used_at = Column(DateTime(timezone=True), nullable=True)
    revoked_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("UserModel", back_populates="refresh_tokens")
