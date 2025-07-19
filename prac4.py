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

