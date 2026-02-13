import secrets
from abc import ABC, abstractmethod

from ..config import settings


class TokenGenerator(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass


class SecureTokenGenerator(TokenGenerator):
    def generate(self) -> str:
        return secrets.token_urlsafe(settings.REFRESH_TOKEN_LENGTH_MAX)
