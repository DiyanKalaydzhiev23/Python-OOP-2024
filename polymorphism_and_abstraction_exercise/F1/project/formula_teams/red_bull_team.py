from typing import Dict
from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @property
    def sponsors(self) -> Dict[str, Dict[int, int]]:
        return {
            "Oracle": {
                1: 1_500_000,
                2: 800_000,
            },
            "Honda": {
                8: 20_000,
                10: 10_000,
            },
        }

    @property
    def expenses(self) -> int:
        return 250_000
