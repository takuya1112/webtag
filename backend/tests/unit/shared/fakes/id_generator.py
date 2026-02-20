from uuid import UUID


class FakeIdGenerator:
    def generate(self) -> UUID:
        return UUID("01900000-0000-7000-8000-000000000001")
