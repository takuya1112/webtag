from access_token.domain.exceptions import (
    ExpiredAccessTokenError,
    InvalidAccessTokenError,
)
from access_token.domain.jwt_service import JwtService
from core.logging import get_logger
from shared.application import UnitOfWork
from user.domain.entity import UserEntity
from user.domain.value_objects import UserId
from user.infrastructure.repository import SQLAlchemyUserRepository

from .exceptions import UserUnauthorizedError

logger = get_logger(__name__)


class GetCurrentUser:
    def __init__(
        self,
        uow: UnitOfWork,
        jwt_service: JwtService,
    ):
        self.uow = uow
        self.jwt_service = jwt_service

    def execute(self, access_token: str) -> UserEntity:
        try:
            user_id = UserId(self.jwt_service.verify(access_token))
        except (ExpiredAccessTokenError, InvalidAccessTokenError):
            logger.warning("Invalid token")
            raise UserUnauthorizedError()

        with self.uow:
            repo = self.uow.get_repo(SQLAlchemyUserRepository)
            user = repo.find_by_id(user_id)

        if not user:
            logger.warning("User not found: user_id=%s", user_id.value)
            raise UserUnauthorizedError()

        if not user.can_login():
            logger.warning("User can't login: user_id=%s", user_id.value)
            raise UserUnauthorizedError()
        return user
