from dataclasses import dataclass

from .exceptions import UserAlreadyActive, UserAlreadyInactive
from .value_objects import (
    UserCreatedAt,
    UserDeactivatedAt,
    UserEmail,
    UserHashedPassword,
    UserId,
    UserName,
    UserUpdatedAt,
)


@dataclass
class UserEntity:
    id: UserId
    name: UserName
    email: UserEmail
    password_hash: UserHashedPassword
    created_at: UserCreatedAt
    updated_at: UserUpdatedAt
    deactivated_at: UserDeactivatedAt | None = None

    @property
    def is_active(self) -> bool:
        return self.deactivated_at is None

    def activate(self, updated_at: UserUpdatedAt) -> None:
        if self.is_active:
            raise UserAlreadyActive()
        self.deactivated_at = None
        self.updated_at = updated_at

    def deactivate(
        self,
        deactivated_at: UserDeactivatedAt,
        updated_at: UserUpdatedAt,
    ) -> None:
        if not self.is_active:
            raise UserAlreadyInactive()
        self.deactivated_at = deactivated_at
        self.updated_at = updated_at

    def change_name(
        self, new_name: UserName, updated_at: UserUpdatedAt
    ) -> None:
        self.name = new_name
        self.updated_at = updated_at

    def change_Useremail(
        self, new_Useremail: UserEmail, updated_at: UserUpdatedAt
    ) -> None:
        self.Useremail = new_Useremail
        self.updated_at = updated_at

    def change_password(
        self,
        new_password_hash: UserHashedPassword,
        updated_at: UserUpdatedAt,
    ) -> None:
        self.password_hash = new_password_hash
        self.updated_at = updated_at

    def can_login(self) -> bool:
        return self.is_active
