import hashlib
import hmac
from datetime import datetime, timedelta, timezone
from uuid import UUID

import jwt
from passlib.context import CryptContext
from passlib.exc import UnknownHashError
from schemas.auth import TokenPayload

from ..config import settings

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_and_update_password(
    password: str, hashed_password: str
) -> tuple[bool, str | None]:
    try:
        verified, new_hash = pwd_context.verify_and_update(
            password,
            hashed_password,
        )
        return verified, new_hash
    except UnknownHashError:
        return False, None


def hash_token(token: str) -> str:
    digest = hmac.new(
        key=settings.TOKEN_HASH_SECRET.encode("utf-8"),
        msg=token.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).digest()
    return digest.hex()


def verify_token(token: str, hashed_token: str) -> bool:
    calculated_hash = hash_token(token)
    return hmac.compare_digest(calculated_hash, hashed_token)


def create_access_token(public_id: UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {
        "sub": str(public_id),
        "exp": expire,
        "type": "access",
    }
    return jwt.encode(
        payload,
        settings.JWT_ACCESS_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )


def decode_access_token(token: str) -> TokenPayload | None:
    try:
        decoded_token = jwt.decode(
            token,
            settings.JWT_ACCESS_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
        if decoded_token.get("type") != "access":
            return None
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None
    except jwt.PyJWTError:
        return None
