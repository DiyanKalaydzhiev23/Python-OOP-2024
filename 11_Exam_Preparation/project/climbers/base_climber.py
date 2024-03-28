from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak
from typing import List


class BaseClimber(ABC):
    STRENGTH_INCREASE: int = 15

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: List[str] = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")

        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")

        self.__strength = value

    @abstractmethod
    def can_climb(self) -> bool:
        pass

    @abstractmethod
    def climb(self, peak: BasePeak) -> None:
        pass

    def rest(self) -> None:
        self.strength += BaseClimber.STRENGTH_INCREASE

    def __str__(self):
        return (f"{self.__class__.__name__}: "
                f"/// Climber name: {self.name} * "
                f"Left strength: {float(self.strength)} * "
                f"Conquered peaks: {', '.join(sorted(self.conquered_peaks))} ///")
