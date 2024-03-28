class ClimbingRobot:
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def __init__(self, category: str, part_type: str, capacity: int, memory: int):
        self.category = category
        self.part_type = part_type
        self.capacity = capacity
        self.memory = memory
        self.installed_software = []

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value not in self.ALLOWED_CATEGORIES:
            raise ValueError(f"Category should be one of {self.ALLOWED_CATEGORIES}")
        self.__category = value

    def get_used_capacity(self):
        return sum(s['capacity_consumption'] for s in self.installed_software)

    def get_available_capacity(self):
        return self.capacity - self.get_used_capacity()

    def get_used_memory(self):
        return sum(s['memory_consumption'] for s in self.installed_software)

    def get_available_memory(self):
        return self.memory - self.get_used_memory()

    def install_software(self, software: {str, int}):
        if self.get_available_capacity() >= software['capacity_consumption'] and \
                self.get_available_memory() >= software['memory_consumption']:
            self.installed_software.append(software)
            return f"Software '{software['name']}' successfully installed on {self.category} part."
        else:
            return f"Software '{software['name']}' cannot be installed on {self.category} part."
