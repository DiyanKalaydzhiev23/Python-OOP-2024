from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    MIN_STRENGTH_NEEDED: float = 100
    INITIAL_STRENGTH_NEEDED: float = 200

    def __init__(self, name: str):
        super().__init__(name, ArcticClimber.INITIAL_STRENGTH_NEEDED)

    def can_climb(self) -> bool:
        return self.strength >= ArcticClimber.MIN_STRENGTH_NEEDED

    def climb(self, peak: BasePeak) -> None:
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)
