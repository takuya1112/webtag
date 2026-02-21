class FakePasswordHasher:
    def hash(self, password: str) -> str:
        return f"hashed_{password}"

    def verify_and_update_password(
        self,
        password: str,
        hashed_password: str,
    ) -> tuple[bool, str | None]:
        return hashed_password == self.hash(password), None
