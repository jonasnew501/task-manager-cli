import os
import sys

from src.task_manager_cli.core.task import Task

class TaskRepository:
    def __init__(self):
        self.tasks = list[Task] = []
    
    def add_task(self, task: Task):
        self.tasks.append(task)
    
    def remove_task(self, task: Task):
        self.tasks.remove(task)
    
    def get_all_tasks(self) -> list[Task]:
        return self.tasks
    
    def save_tasks_to_file(self, filename: str):
        path_to_output_folder = self._get_folderpath_for_output()

        path_to_output_file = os.path.realpath(os.path.join(path_to_output_folder, filename))

        with open(file=path_to_output_file, mode='w') as f:
            for task_id, task in enumerate(self.tasks):
                f.write(f"task_id: {task_id}, task: {task}\n")
    
    def load_tasks_from_file(self, filename: str):
        path_to_output_folder = self._get_folderpath_for_output()
        
        path_to_output_file = os.path.realpath(os.path.join(path_to_output_folder, filename))

        with open(file=path_to_output_file, mode='r') as f:
            self.tasks = f.read()
    
    def mark_completed(self, task_id: int):
        all_tasks = self.get_all_tasks()

        all_tasks[task_id].mark_completed()
    
    def update_task_description(self, task_id: int, new_description: str):
        all_tasks = self.get_all_tasks()

        all_tasks[task_id].update_description(new_description)
    
    def update_task_category(self, task_id: int, new_category: str):
        all_tasks = self.get_all_tasks()

        all_tasks[task_id].update_category(new_category)


    
    def _get_folderpath_for_output(self):
        cwd = os.getcwd()

        output_folder = self._get_foldername_for_output()

        filepath = os.path.join(cwd, output_folder)

        filepath_real = os.path.realpath(filepath)

        return filepath_real
    
    def _get_foldername_for_output(self):
        cwd = os.getcwd()

        possible_output_names = ["output", "outputs", "tasks"]

        output_folder = next((name for name in possible_output_names if name in os.listdir(cwd)), None)

        if output_folder is None:
            raise FileNotFoundError("No valid output folder found")
        
        return output_folder



