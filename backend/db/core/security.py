from passlib.context import CryptContext
from passlib.exc import UnknownHashError

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