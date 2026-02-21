from user.domain.entity import UserEntity
from user.domain.value_objects import Email, UserId


class FakeUserRepository:
    def __init__(self):
        self.store: list[UserEntity] = []

    def add(self, user: UserEntity) -> None:
        self.store.append(user)

    def update(self, user: UserEntity) -> None:
        for index, u in enumerate(self.store):
            if user.id == u.id:
                self.store[index] = user
                return
        raise ValueError("User not found by user id: %s", user.id.value)

    def find_by_id(self, user_id: UserId) -> UserEntity | None:
        return next(
            (user for user in self.store if user.id == user_id),
            None,
        )

    def find_by_email(self, email: Email) -> UserEntity | None:
        return next(
            (user for user in self.store if user.email == email),
            None,
        )
