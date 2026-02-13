from core.config import settings
from core.session import Base
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    String,
    func,
)
from sqlalchemy.orm import relationship


class RefreshTokenModel(Base):
    __tablename__ = "refresh_tokens"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    hashed_token = Column(
        String(settings.DB_REFRESH_TOKEN_LENGTH_MAX),
        unique=True,
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    expires_at = Column(DateTime(timezone=True), index=True, nullable=False)
    revoked_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="refresh_tokens")
