from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):
    MIN_BUDGET: int = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses_for_one_race(self) -> int:
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < FormulaTeam.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue: int = 0

        for sponsor in self.sponsors.values():  # [{1: 1_500_000, 2: 800_000}, {8: 20_000, 10: 10_000}]
            for pos in sponsor:  # {1: 1_500_000, 2: 800_000} - should be sorted
                if race_pos <= pos:
                    revenue += sponsor[pos]
                    break

        revenue -= self.expenses_for_one_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
