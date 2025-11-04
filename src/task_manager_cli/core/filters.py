from abc import ABC, abstractmethod

class TaskFilter(ABC):
    @abstractmethod
    def match(self, task) -> bool:
        pass