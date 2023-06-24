from typing import List
from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        tasks_count = len(self.tasks)

        self.tasks.clear()

        return f"Cleared {tasks_count} tasks."

    def view_section(self) -> str:
        tasks = '\n'.join([t.details() for t in self.tasks])

        return f"Section {self.name}:\n" + \
               f"{tasks}"
