from dataclasses import dataclass

from .exceptions import UserAlreadyActive, UserAlreadyInactive
from .value_objects import (
    CreatedAt,
    DeactivatedAt,
    Email,
    HashedPassword,
    UpdatedAt,
    UserId,
    UserName,
)


@dataclass
class UserEntity:
    id: UserId
    name: UserName
    email: Email
    password_hash: HashedPassword
    created_at: CreatedAt
    updated_at: UpdatedAt
    deactivated_at: DeactivatedAt | None = None

    @property
    def is_active(self) -> bool:
        return self.deactivated_at is None

    def activate(self, updated_at: UpdatedAt) -> None:
        if self.is_active:
            raise UserAlreadyActive()
        self.deactivated_at = None
        self.updated_at = updated_at

    def deactivate(
        self,
        deactivated_at: DeactivatedAt,
        updated_at: UpdatedAt,
    ) -> None:
        if not self.is_active:
            raise UserAlreadyInactive()
        self.deactivated_at = deactivated_at
        self.updated_at = updated_at

    def change_name(self, new_name: UserName, updated_at: UpdatedAt) -> None:
        self.name = new_name
        self.updated_at = updated_at

    def change_email(self, new_email: Email, updated_at: UpdatedAt) -> None:
        self.email = new_email
        self.updated_at = updated_at

    def change_password(
        self,
        new_password_hash: HashedPassword,
        updated_at: UpdatedAt,
    ) -> None:
        self.password_hash = new_password_hash
        self.updated_at = updated_at

    def can_login(self) -> bool:
        return self.is_active
