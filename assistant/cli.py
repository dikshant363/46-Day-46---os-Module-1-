from .task_manager import TaskManager
from .task import Task

class CLI:
    def __init__(self):
        self.task_manager = TaskManager()

    def run(self):
        print("Welcome to your Personal AI Secretary!")
        while True:
            print("\nWhat would you like to do?")
            print("1. Add a new task")
            print("2. List all tasks")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.list_tasks()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_task(self):
        title = input("Enter task title: ")
        if not title:
            print("Title cannot be empty.")
            return

        category = input("Enter category (e.g., Work, Personal) [Personal]: ") or "Personal"
        priority = input("Enter priority (High, Medium, Low) [Medium]: ") or "Medium"

        task = Task(title=title, category=category, priority=priority)
        self.task_manager.add_task(task)
        print("Task added successfully!")

    def list_tasks(self):
        tasks = self.task_manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")
            print("------------------")
