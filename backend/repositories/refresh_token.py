from sqlalchemy import and_
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from db.models import RefreshToken
from core import get_logger, TokenNotExistError


logger = get_logger(__name__)

class RefreshTokenRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_token(self, hashed_token: str) -> RefreshToken | None:
        return (
            self.session
            .query(RefreshToken)
            .filter(RefreshToken.hashed_token == hashed_token)
            .one_or_none()
        )
    
    def get_by_token_or_raise(self, hashed_token: str) -> RefreshToken:
        refresh_token = (
            self.session
            .query(RefreshToken)
            .filter(and_(
                RefreshToken.hashed_token == hashed_token,
                RefreshToken.revoked_at.is_(None),
                RefreshToken.expires_at > datetime.now(timezone.utc)
            )).one_or_none()
        )
        if not refresh_token:
            logger.warning("Refresh token not exist")
            raise TokenNotExistError
        return refresh_token

    def add(self, user_id: int, hashed_token: str, expires_at: datetime) -> None:
        refresh_token = RefreshToken(
            user_id=user_id,
            hashed_token=hashed_token,
            expires_at=expires_at,
        )
        self.session.add(refresh_token)
        logger.info("Refresh token added successfully")

    def delete(self, hashed_token: str) -> None:
        refresh_token = self.get_by_token_or_raise(hashed_token)
        refresh_token.revoked_at = datetime.now(timezone.utc)
        logger.info("Refresh token deleted successfully")