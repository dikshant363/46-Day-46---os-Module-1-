import json
from .task import Task

class TaskManager:
    def __init__(self, tasks_file='assistant/tasks.json'):
        self.tasks_file = tasks_file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.tasks_file, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(data) for data in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open(self.tasks_file, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def get_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            return self.tasks[task_index]
        return None

    def list_tasks(self):
        return self.tasks

    def update_task(self, task_index, **kwargs):
        task = self.get_task(task_index)
        if task:
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            self.save_tasks()
            return True
        return False

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()
            return True
        return False
