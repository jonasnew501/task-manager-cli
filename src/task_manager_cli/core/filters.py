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


# Just to show:
# The following approach would violate the Open-Closed-Principle,
# because in order to extend the functionality (i.e. when adding
# a new filter-type and it's filtering-condition), a new if-statement
# would have to be added, and thus the 'match'-function would need
# to be modified (i.e. the 'match'-function would be open for extension,
# but would NOT be closed for modification!)
"""
class Filter:
    def match(task, concreteFilter) -> bool:
        if concreteFilter == "FilterA":
            return task.completed()
        if concreteFilter == "FilterB":
            return task.category == "SomeCategory"
"""
        
        