from passlib.context import CryptContext
from passlib.exc import UnknownHashError
from datetime import datetime, timedelta, timezone
import jwt
from uuid import UUID
from .config import settings

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password (password: str) -> str:
    return pwd_context.hash(password)

def verify_and_update_password(
        password: str, 
        hashed_password: str
    ) -> tuple[bool, str | None]:
    try:
        verified, new_hash = pwd_context.verify_and_update(password, hashed_password)
        return verified, new_hash
    except UnknownHashError:
        return False, None

def create_access_token(public_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub" : public_id,
        "exp" : expire,
    }
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

def decode_access_token(token : str) -> dict | None:
    try:
        decoded_token = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None
    except jwt.PyJWTError:
        return None