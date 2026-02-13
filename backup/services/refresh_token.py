from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from uuid import UUID
from db.models import RefreshToken
from repositories import RefreshTokenRepository
from core import (
    settings, TokenNotExistError,
    get_logger, hash_token,
    create_refresh_token,
) 

logger = get_logger(__name__)

class RefreshTokenService:
    def __init__(self, session: Session):
        self.repo = RefreshTokenRepository(session)

    def create_and_add(self, user_id: int, public_id: UUID) -> str:
        refresh_token = create_refresh_token(public_id)
        hashed_token = hash_token(refresh_token)
        expires_at = datetime.now(timezone.utc) + timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS
        )
        self.repo.add(
            user_id=user_id, 
            hashed_token=hashed_token,
            expires_at=expires_at,
        )
        return refresh_token
    
    def revoke(self, token: str) -> None:
        hashed_token = hash_token(token)
        self.repo.delete(hashed_token)
