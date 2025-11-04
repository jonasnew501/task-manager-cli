
class Task:
    def __init__(self, description: str, category: str, completed: bool):
        self.description = description
        self.category = category
        self.completed = completed
    
    def update_description(self, new_description: str):
        self.description = new_description
    
    def update_category(self, new_category: str):
        self.category = new_category

    def mark_completed(self):
        self.completed = True
