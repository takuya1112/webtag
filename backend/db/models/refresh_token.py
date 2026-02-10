from sqlalchemy import (
    Column, BigInteger, String, DateTime, Index,
    ForeignKey, func,
)
from sqlalchemy.orm import relationship
from ..session import Base
from core.constants import RefreshTokenConfig


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(
        BigInteger, 
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False,
    )
    token_hash = Column(
        String(RefreshTokenConfig.DB_TOKEN_LENGTH_MAX), 
        unique=True, 
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    expires_at = Column(DateTime(timezone=True), nullable=False)
    revoked_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="refresh_tokens")

    __table_args__ = (
        Index(
            "ix_refresh_tokens_user_active",
            user_id,
            postgresql_where=(revoked_at.is_(None)),
        ),
        Index(
            "ix_refresh_tokens_expires",
            expires_at,
            postgresql_where=(revoked_at.is_(None)),
        ),
        Index(
            "ix_refresh_tokens_cleanup",
            expires_at,
            postgresql_where=(revoked_at.isnot(None)),
        ),
    )