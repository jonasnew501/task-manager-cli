from src.task_manager_cli.core.taskRepository import TaskRepository
from src.task_manager_cli.core.task import Task


class TaskManager:
    def __init__(self, taskRepository: TaskRepository):
        self.taskRepository = taskRepository
    
    def add_task(self, description: str, category: str = "", completed: bool = False):
        new_task = self._create_new_task(description=description, category=category, completed=completed)

        self.taskRepository.add_task(task=new_task)
    
    def complete_task(self, task_id: int):
        all_tasks = self.taskRepository.get_all_tasks()

        all_tasks[task_id].mark_completed()
    
    def update_task_description(self, task_id: int, new_description: str):
        all_tasks = self.taskRepository.get_all_tasks()

        all_tasks[task_id].update_description(new_description)
    
    def update_task_category(self, task_id: int, new_category: str):
        all_tasks = self.taskRepository.get_all_tasks()

        all_tasks[task_id].update_category(new_category)
    
    #TODO: Implement
    # def list_tasks(self, filters: list[Filter] = None) -> list[Task]:
        

    
    def _create_new_task(self, description: str, category: str, completed: bool) -> Task:
        task = Task(description=description, category=category, completed=completed)

        return task