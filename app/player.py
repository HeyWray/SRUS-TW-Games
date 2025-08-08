"""
The identity of the player with name and uid
"""

class Player():
    def __init__(self, uid: str, player_name: str):
        self._uid = uid
        self._player_name = player_name

    def __str__(self) -> str:
        return f"Player: {self.player_name}, ID: {self.uid}"

    # <editor-fold desc="Properties and Setters">
    @property
    def uid(self) -> str:
        return self._uid

    #Two variations for player names
    @property
    def player_name(self) -> str:
        return self._player_name

    @property
    def name(self) -> str:
        return self.player_name
    # </editor-fold>