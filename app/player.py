"""
The identity of the player
"""

class Player():
    def __init__(self, uid: str, player_name: str):
        self._uid = uid
        self._player_name = player_name

    def uid(self) -> str:
        return self._uid

    def player_name(self) -> str:
        return self._player_name

    def __str__(self):
        return f"Player called {self.player_name()} with ID of {self.uid()}"
