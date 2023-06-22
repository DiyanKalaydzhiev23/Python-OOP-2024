from typing import List


class SteamUser:
    def __init__(self, username: str, games: List[str]):
        self.username = username
        self.games = games
        self.played_hours: int = 0

    def play(self, game: str, hours: int) -> str:
        if game not in self.games:
            return f"{game} is not in library"

        self.played_hours += hours

        return f"{self.username} is playing {game}"

    def buy_game(self, game: str) -> str:
        if game in self.games:
            return f"{game} is already in your library"

        self.games.append(game)

        return f"{self.username} bought {game}"

    def status(self) -> str:
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


user = SteamUser("Peter", ["Rainbow SixSiege", "CS:GO", "Fortnite"])

print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))

print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
