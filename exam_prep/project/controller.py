from typing import Tuple, List
from project.player import Player
from project.supply.supply import Supply


class Controller:
    VALID_TYPES = [
        "Food",
        "Drink"
    ]

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Tuple[Player]) -> str:
        players_added = []

        for player in players:
            if player not in self.players:
                self.players.append(player)
                players_added.append(player.name)

        return f"Successfully added: {', '.join(players_added)}"

    def add_supply(self, *supplies: Tuple[Supply]) -> None:
        [self.supplies.append(s) for s in supplies]

    def sustain(self, player_name: str, sustenance_type: str) -> str or None:
        if sustenance_type not in self.VALID_TYPES:
            return

        for player in self.players:
            if player.name == player_name:
                break
        else:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[i]

            if supply.__class__.__name__ == sustenance_type:
                self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + supply.energy, 100)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str) -> str:
        current_players = sorted([
            next(filter(lambda p: p.name == first_player_name, self.players)),
            next(filter(lambda p: p.name == second_player_name, self.players)),
        ], key=lambda p: p.stamina)  # marker

        errors_list = []

        for player in current_players:
            if player.stamina <= 0:
                errors_list.append(f"Player {player.name} does not have enough stamina.")

        if errors_list:
            return "\n".join(errors_list)

        return self.fight(current_players)

    def fight(self, current_players: List[Player]) -> str:
        first_player_damage = current_players[0].stamina / 2
        current_players[1].stamina = max(current_players[1].stamina - first_player_damage, 0)

        second_player_damage = current_players[1].stamina / 2
        current_players[0].stamina = max(current_players[0].stamina - second_player_damage, 0)

        winner = sorted(current_players, key=lambda p: -p.stamina)[0]

        return f"Winner: {winner.name}"

    def next_day(self) -> None:
        for player in self.players:
            reduce_stamina_with = player.age * 2
            player.stamina = max(player.stamina - reduce_stamina_with, 0)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        return "\n".join(
            [str(p) for p in self.players]
                +
            [s.details() for s in self.supplies]
        )
