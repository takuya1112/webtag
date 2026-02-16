from abc import ABC, abstractmethod

from .value_objects import AwareDatetime


class Clock(ABC):
    @abstractmethod
    def now(self) -> AwareDatetime:
        pass
