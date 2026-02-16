import secrets

from core.constants import RefreshTokenConfig

from ...domain.security import TokenGenerator


class SecureTokenGenerator(TokenGenerator):
    def generate(self) -> str:
        return secrets.token_urlsafe(
            RefreshTokenConfig.REFRESH_TOKEN_LENGTH_MAX
        )
