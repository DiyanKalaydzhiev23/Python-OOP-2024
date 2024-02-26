from typing import List


class User:

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books: List[str] = []

    def info(self) -> str:
        return ", ".join(sorted(self.books)) or "[]"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.info()}"
