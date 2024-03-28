from typing import List
from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.summit_peak import SummitPeak
from project.peaks.arctic_peak import ArcticPeak


class SummitQuestManagerApp:
    VALID_CLIMBER_TYPES = {
        "ArcticClimber": ArcticClimber,
        "SummitClimber": SummitClimber,
    }

    VALID_PEAKS_TYPES = {
        "ArcticPeak": ArcticPeak,
        "SummitPeak": SummitPeak,
    }

    def __init__(self):
        self.peaks: List[BasePeak] = []
        self.climbers: List[BaseClimber] = []

    def register_climber(self, climber_type: str, climber_name: str) -> str:
        try:
            climber = self.VALID_CLIMBER_TYPES[climber_type](climber_name)
        except KeyError:
            return f"{climber_type} doesn't exist in our register."

        try:
            next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            self.climbers.append(climber)
            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
        try:
            peak = self.VALID_PEAKS_TYPES[peak_type](peak_name, peak_elevation)
        except KeyError:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]) -> str:
        climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))

        if gear == peak.get_recommended_gear():
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False

        return (f"{climber_name} is not prepared to climb {peak_name}. "
                f"Missing gear: "
                f"{', '.join(g for g in sorted(peak.get_recommended_gear()) if g not in gear)}.")

    def perform_climbing(self, climber_name: str, peak_name: str) -> str:
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)

        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self) -> str:
        climbers_that_can_climb = filter(lambda c: len(c.conquered_peaks) > 0, self.climbers)
        climbers = sorted(climbers_that_can_climb, key=lambda c: (-len(c.conquered_peaks), c.name))

        total_peaks_climbed = len({p for c in climbers for p in c.conquered_peaks})

        return f"Total climbed peaks: {total_peaks_climbed}\n" + \
                "**Climber's statistics:**\n" + \
                "\n".join(str(c) for c in climbers)
