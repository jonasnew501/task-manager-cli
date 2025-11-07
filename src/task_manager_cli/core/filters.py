from abc import ABC, abstractmethod
import sys
import inspect


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




class FilterUtilities:
    def __init__(self):
        pass

    def get_all_concrete_filters(self, parent_class=None) -> list[str]:
        """
        Retrieves the names of all classes in this file,
        which inherit from 'parent_class'.
        Those are all concrete filters.

        Args:
            parent_class (class): A specific class which every concrete filter class
                                  needs to inherit from.

        Returns:
            list[str]: A list containing the names of all
                    concrete filters listed in this
                    file.
        """
        all_classes = self._get_all_classes_of_current_module()
        classes_defined_in_current_module = self._filter_classes_defined_in_current_module(classes=all_classes)
        print(classes_defined_in_current_module[0][0])
        print(classes_defined_in_current_module[0][1])
        print(type(classes_defined_in_current_module[0][1]))
        raise Exception

        classes_interiting_from_parent_class = self._filter_classes_inheriting_from_specific_class(parent_class=parent_class, classes=all_classes)

        concrete_filters = set(classes_defined_in_current_module).intersection(set(classes_interiting_from_parent_class))

        concrete_filters_names = [cls.__name__ for cls in concrete_filters]
        return concrete_filters_names
    
    def get_classes_from_strings(self, classes: list[tuple[str]], classes_in_user_input: list[str]) -> list[str]:
        """
        Returns a list of classes (as strings), whose name(s) matches the class names
        specified in 'classes_in_user_input'.

        Args:
            classes (list[tuple[str]]): A list holding the name of the class and the corresponding
                                        class specification.
                                        E.g. ['TestClass2', '']
        """


    def _get_all_classes_of_current_module(self) -> list[tuple[str]]:
        current_module = sys.modules[__name__]
        all_classes = inspect.getmembers(current_module, inspect.isclass)
        return all_classes

    def _filter_classes_defined_in_current_module(self, classes: list[tuple[str]]) -> list[tuple[str]]:
        """
        Filters 'classes' to only classes that are defined in the
        current module (i.e. excluding classes imported into this module).
        """
        current_module = sys.modules[__name__]
        classes_defined_in_current_module = [(name, cls) for name, cls in classes if cls.__module__ == current_module.__name__]

        return classes_defined_in_current_module

    def _filter_classes_inheriting_from_specific_class(self, parent_class, classes: list[tuple[str]]) -> list[tuple[str]]:
        """
        Filters 'classes' to only classes that inherit (directly or indirectly)
        from 'parent_class', but are not 'parent_class' itself.
        """
        if parent_class is None:
            return []
        
        classes_interiting_from_parent_class = [cls for name, cls in classes if issubclass(cls, parent_class) and cls is not parent_class]
        return classes_interiting_from_parent_class





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
        
        