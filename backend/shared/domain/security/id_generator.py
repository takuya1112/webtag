from abc import ABC, abstractmethod

from ..value_objects import AppUuid


class IdGenerator(ABC):
    @abstractmethod
    def generate(self) -> AppUuid:
        pass
