from typing import List


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed: bool = False

    def change_name(self, new_name: str) -> str:
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name

        return new_name

    def change_due_date(self, new_due_date: str) -> str:
        if self.due_date == new_due_date:
            return "Date cannot be the same."

        self.due_date = new_due_date

        return new_due_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_idx: int, new_comment: str) -> str:
        if not 0 <= comment_idx < len(self.comments):
            return "Cannot find comment."

        self.comments[comment_idx] = new_comment

        return ', '.join(self.comments)

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"
