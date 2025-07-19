import json
import os

TASKS_FILE = "tasks.json"
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {"description": self.description, "completed": self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data["description"], data["completed"])
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(d) for d in data]

def save_tasks(self):
        with open(TASKS_FILE, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_tasks()
        print("✅ Task added.")

def menu():
    manager = TaskManager()
    while True:
        print("\n=== Task Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

choice = input("Choose an option (1-5): ")
        if choice == '1':
            manager.view_tasks()
        elif choice == '2':
            desc = input("Enter task description: ")
            manager.add_task(desc)
        elif choice == '3':
            manager.view_tasks()
            try:
                index = int(input("Task number to mark complete: ")) - 1
                manager.complete_task(index)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            manager.view_tasks()
            try:
                index = int(input("Task number to delete: ")) - 1
                manager.delete_task(index)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            print("👋 Exiting Task Manager.")
            break
        else:
            print("❌ Invalid choice. Try again.")


menu()
