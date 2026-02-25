from core.logging import get_logger
from shared.application.uow import UnitOfWork
from shared.domain.security import PasswordHasher

from ..domain.factory import UserFactory
from ..domain.repository import UserRepository
from ..domain.value_objects import Email, HashedPassword, UserId, UserName
from ..exceptions.http import EmailAlreadyExistError

logger = get_logger(__name__)


class CreateUser:
    def __init__(
        self,
        uow: UnitOfWork,
        repository: type[UserRepository],
        factory: UserFactory,
        password_hasher: PasswordHasher,
    ):
        self.uow = uow
        self.repository = repository
        self.factory = factory
        self.password_hasher = password_hasher

    def execute(self, name: str, email: str, password: str) -> UserId:
        with self.uow:
            repo = self.uow.get_repo(self.repository)
            name_vo = UserName(name)
            email_vo = Email(email)

            if repo.find_by_email(email_vo):
                logger.warning("Email already exist")
                raise EmailAlreadyExistError(message="Email already exist")

            password_hash_vo = HashedPassword(
                self.password_hasher.hash(password)
            )
            entity = self.factory.create(
                name=name_vo,
                email=email_vo,
                password_hash=password_hash_vo,
            )
            repo.add(entity)
            self.uow.commit()
        logger.info("user is added: user_id=%s", entity.id.value)
        return entity.id
