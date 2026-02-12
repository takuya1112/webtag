import hashlib
import hmac
from abc import ABC, abstractmethod

from ..config import settings


class TokenHasher(ABC):
    @abstractmethod
    def hash(self, token: str) -> str:
        pass

    @abstractmethod
    def verify(self, token: str, hashed_token: str) -> bool:
        pass


class HMACHasher(TokenHasher):
    def hash(self, token: str) -> str:
        digest = hmac.new(
            key=settings.TOKEN_HASH_SECRET.encode("utf-8"),
            msg=token.encode("utf-8"),
            digestmod=hashlib.sha256,
        ).digest()
        return digest.hex()

    def verify(self, token: str, hashed_token: str) -> bool:
        calculated_hash = self.hash(token)
        return hmac.compare_digest(calculated_hash, hashed_token)
