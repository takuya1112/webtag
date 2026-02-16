from abc import ABC, abstractmethod


class TokenHasher(ABC):
    @abstractmethod
    def hash(self, token: str) -> str:
        pass

    @abstractmethod
    def verify(self, token: str, hashed_token: str) -> bool:
        pass
