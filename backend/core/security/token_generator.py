import secrets
from abc import ABC, abstractmethod

from ..constants import RefreshTokenConfig


class TokenGenerator(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass


class SecureTokenGenerator(TokenGenerator):
    def generate(self) -> str:
        return secrets.token_urlsafe(RefreshTokenConfig.REFRESH_TOKEN_LENGTH_MAX)
