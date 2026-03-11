import secrets

from core.constants import RefreshTokenConfig


class SecureRefreshTokenGenerator:
    def generate(self) -> str:
        return secrets.token_urlsafe(
            RefreshTokenConfig.REFRESH_TOKEN_LENGTH_MAX
        )
