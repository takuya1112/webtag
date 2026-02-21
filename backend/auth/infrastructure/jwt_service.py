from datetime import timedelta
from uuid import UUID

import jwt
from shared.domain.clock import Clock

from ..exceptions.domain import ExpiredAccessTokenError, InvalidAccessTokenError


class PyJwtService:
    def __init__(
        self,
        secret: str,
        algorithm: str,
        expire_minutes: int,
        clock: Clock,
    ):
        self.secret = secret
        self.algorithm = algorithm
        self.expire_minutes = expire_minutes
        self.clock = clock

    def issue(self, user_id: UUID) -> str:
        expire = self.clock.now() + timedelta(minutes=self.expire_minutes)

        payload = {
            "sub": str(user_id),
            "exp": expire,
            "type": "access",
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm=self.algorithm,
        )

    def verify(self, token: str) -> UUID:
        try:
            decoded_token = jwt.decode(
                token,
                self.secret,
                algorithms=[self.algorithm],
            )
            if decoded_token.get("type") != "access":
                raise InvalidAccessTokenError() from None
            return UUID(decoded_token["sub"])
        except jwt.ExpiredSignatureError:
            raise ExpiredAccessTokenError() from None
        except jwt.PyJWTError:
            raise InvalidAccessTokenError() from None
