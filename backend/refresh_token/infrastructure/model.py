from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from core.constants import RefreshTokenConfig
from shared.infrastructure.base import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from user.infrastructure.model import UserModel


class RefreshTokenModel(Base):
    """RefreshToken Model"""

    __tablename__ = "refresh_tokens"
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
    )
    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    token_hash: Mapped[str] = mapped_column(
        String(RefreshTokenConfig.DB_REFRESH_TOKEN_LENGTH_MAX),
        unique=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        index=True,
    )
    used_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    revoked_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    user: Mapped[UserModel] = relationship(
        back_populates="refresh_tokens",
    )
