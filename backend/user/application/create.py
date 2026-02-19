from core.logging import get_logger
from shared.domain.security import PasswordHasher

from ..domain.factory import UserFactory
from ..domain.repository import UserRepository
from ..domain.value_objects import Email, HashedPassword, UserId, UserName
from ..exceptions.http import EmailAlreadyExistError

logger = get_logger(__name__)


class CreateUser:
    def __init__(
        self,
        repository: UserRepository,
        factory: UserFactory,
        password_hasher: PasswordHasher,
    ):
        self.repository = repository
        self.factory = factory
        self.password_hasher = password_hasher

    def execute(self, name: str, email: str, password: str) -> UserId:
        name_vo = UserName(name)
        email_vo = Email(email)

        if self.repository.find_by_email(email_vo):
            logger.warning("Email already exist")
            raise EmailAlreadyExistError()

        password_hash_vo = HashedPassword(self.password_hasher.hash(password))
        entity = self.factory.create(
            name=name_vo,
            email=email_vo,
            password_hash=password_hash_vo,
        )
        self.repository.add(entity)
        return entity.id
