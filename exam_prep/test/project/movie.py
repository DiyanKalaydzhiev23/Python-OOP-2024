class Movie:
    def __init__(self, name: str, year: int, rating: float):
        self.name = name
        self.year = year
        self.rating = rating
        self.actors = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be an empty string!")

        self.__name = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1887:
            raise ValueError("Year is not valid!")

        self.__year = value

    def add_actor(self, name: str):
        if name not in self.actors:
            self.actors.append(name)
        else:
            return f"{name} is already added in the list of actors!"

    def __gt__(self, other):
        if self.rating > other.rating:
            return f'"{self.name}" is better than "{other.name}"'
        else:
            return f'"{other.name}" is better than "{self.name}"'

    def __repr__(self):
        return f"Name: {self.name}\n" \
               f"Year of Release: {self.year}\n" \
               f"Rating: {self.rating:.2f}\n" \
               f"Cast: {', '.join(self.actors)}"