from dataclasses import dataclass

from shared.domain.value_objects import AwareDatetime, PublicId

from ..exceptions import UserAlreadyActive, UserAlreadyInactive
from .value_objects import Email, HashedPassword, UserName


@dataclass
class UserEntity:
    public_id: PublicId
    name: UserName
    email: Email
    password_hash: HashedPassword
    created_at: AwareDatetime
    updated_at: AwareDatetime
    deactivated_at: AwareDatetime | None = None

    @property
    def is_active(self) -> bool:
        return self.deactivated_at is None

    def activate(self, now: AwareDatetime) -> None:
        if self.is_active:
            raise UserAlreadyActive()
        self.deactivated_at = None
        self.updated_at = now

    def deactivate(self, now: AwareDatetime) -> None:
        if not self.is_active:
            raise UserAlreadyInactive()
        self.deactivated_at = now
        self.updated_at = now

    def change_name(self, new_name: UserName, now: AwareDatetime) -> None:
        self.name = new_name
        self.updated_at = now

    def change_password(
        self,
        new_password_hash: HashedPassword,
        now: AwareDatetime,
    ) -> None:
        self.password_hash = new_password_hash
        self.updated_at = now

    def change_email(self, new_email: Email, now: AwareDatetime) -> None:
        self.email = new_email
        self.updated_at = now

    def can_login(self) -> bool:
        return self.is_active
