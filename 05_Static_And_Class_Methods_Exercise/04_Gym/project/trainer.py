from project.next_id_mixin import NextIdMixin


class Trainer(NextIdMixin):
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
