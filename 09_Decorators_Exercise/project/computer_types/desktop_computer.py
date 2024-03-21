from typing import Dict
from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    @property
    def type(self) -> str:
        return "desktop computer"

    @property
    def available_processors(self) -> Dict[str, int]:
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800,
        }

    @property
    def max_ram(self) -> int:
        return 128
