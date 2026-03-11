from access_token.domain.jwt_service import JwtService
from core.logging import get_logger
from refresh_token.application import CreateRefreshToken
from user.application import CreateUser

logger = get_logger(__name__)


class Signup:
    def __init__(
        self,
        create_user: CreateUser,
        create_refresh_token: CreateRefreshToken,
        jwt_service: JwtService,
    ):
        self.create_user = create_user
        self.create_refresh_token = create_refresh_token
        self.jwt_service = jwt_service

    def execute(self, name: str, email: str, password: str) -> tuple[str, str]:
        user_id = self.create_user.execute(
            name=name,
            email=email,
            password=password,
        )
        refresh_token = self.create_refresh_token.execute(user_id.value)
        access_token = self.jwt_service.issue(user_id.value)
        logger.info("User singed up: user_id=%s", user_id.value)
        return access_token, refresh_token
