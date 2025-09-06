"""
The identity of the player with name and uid
"""

class Player():
    def __init__(self, uid: str, player_name: str):
        self._uid = uid
        self._player_name = player_name

    def __str__(self) -> str:
        return f"Player: {self.name}, ID: {self.uid}"


    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._player_name



    @classmethod
    def create_random_player(cls):
        """Handles creating a new player
            If no name or uid is specified then creates a random name and uid
            """
        import random

        uid = str(random.randrange(
                100, 1000))
        name = random.choice(
                ["Nagz", "Ray", "Bluto", "Heavenly"])

        return cls(uid, name)

    def __eq__(self, other):
        return self.uid == other.uid

    def hash_method(key: str) -> int:
        return hash(key)

    def __hash__(self):
        return self.hash_method(self.uid)