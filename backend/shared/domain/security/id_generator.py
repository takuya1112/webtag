from abc import ABC, abstractmethod
from uuid import UUID


class IdGenerator(ABC):
    @abstractmethod
    def generate(self) -> UUID:
        pass
