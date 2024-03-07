class Category:

    def __init__(self, _id: int, name: str):
        self.id = _id
        self.name = name

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
