from abc import ABC, abstractmethod

class Schedulable(ABC):
    @abstractmethod
    def get_deadline(self) -> int:
        pass
