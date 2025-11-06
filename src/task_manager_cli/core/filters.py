from abc import ABC, abstractmethod

from src.task_manager_cli.core.task import Task

class TaskFilter(ABC):
    @abstractmethod
    def match(self, task: Task) -> bool:
        pass


class CategoryFilter(TaskFilter):
    def __init__(self, category: str) -> None:
        self.category = category
    
    def match(self, task: Task) -> bool:
        return task.category == self.category

class CompletedFiler(TaskFilter):
    def match(self, task: Task) -> bool:
        return task.completed
        