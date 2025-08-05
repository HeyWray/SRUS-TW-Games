
class Player():
    def __init__(self, id: str, player_name: str):
        self._id = id
        self._player_name = player_name

    def id(self) -> str:
        return self._id

    def player_name(self) -> str:
        return self._player_name

    def __str__(self):
        return f"Player called {self.player_name()} with ID of {self.id()}"
