from access_token.domain.jwt_service import JwtService
from core.logging import get_logger
from refresh_token.application import CreateRefreshToken
from shared.application import UnitOfWork
from user.domain.password_hasher import PasswordHasher
from user.domain.repository import UserRepository
from user.domain.value_objects import Email

from .exceptions import InvalidCredentialsError

logger = get_logger(__name__)


class Login:
    def __init__(
        self,
        uow: UnitOfWork,
        repository: type[UserRepository],
        create_refresh_token: CreateRefreshToken,
        jwt_service: JwtService,
        password_hasher: PasswordHasher,
    ):
        self.uow = uow
        self.repository = repository
        self.create_refresh_token = create_refresh_token
        self.jwt_service = jwt_service
        self.password_hasher = password_hasher

    def execute(self, email: str, password: str) -> tuple[str, str]:
        with self.uow:
            repo = self.uow.get_repo(self.repository)
            email_vo = Email(email)
            user = repo.find_by_email(email_vo)

            if not user:
                logger.warning("Email or password Wrong")
                raise InvalidCredentialsError()
            if not user.can_login():
                logger.warning(
                    "User not allowed to login: user_id=%s",
                    user.id.value,
                )
                raise InvalidCredentialsError()

            verified, new_hash = (
                self.password_hasher.verify_and_update_password(
                    password=password,
                    hashed_password=user.password_hash.value,
                )
            )
            if not verified:
                logger.warning("Email or password Wrong")
                raise InvalidCredentialsError()

            # TODO update new hash commit error
            # if new_hash:
            #     hashed_password = HashedPassword(new_hash)
            #     user.change_password(hashed_password, now_vo)
            #     repo.update(user)
            self.uow.commit()

        refresh_token = self.create_refresh_token.execute(user.id.value)
        access_token = self.jwt_service.issue(user.id.value)
        logger.info("User login: user_id=%s", user.id.value)
        return access_token, refresh_token
