class Pokemon:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def pokemon_details(self) -> str:
        return f"{self.name} with health {self.health}"
