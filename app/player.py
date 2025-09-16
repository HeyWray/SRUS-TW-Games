"""
The identity of the player with name and uid
"""

class Player():
    def __init__(self, uid: str, player_name: str, score: int | None = 0):
        self._uid = uid
        self._player_name = player_name
        self._score = score

    def __str__(self) -> str:
        return f"Player: {self.name}, ID: {self.uid}, Score: {self.score}"

    def __hash__(self):
        return self.hash_method(self.uid)

    def __eq__(self, other):
        return self.uid == other.uid

    def __lt__(self, other):
        return self.score < other.score

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._player_name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int):
        if value < 0:
            raise ValueError("Please set a score equal to or greater then 0")
        self._score = value

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
        score = random.randint(0, 100)

        return cls(uid, name, score)

    def hash_method(key: str) -> int:
        return hash(key)

    @classmethod
    def sort_by_descending_score(cls, player_array):
        if len(player_array) <= 1:
            return player_array

        pivot = player_array[len(player_array) // 2]
        less_than = []
        greater_than = []

        for i in player_array[1:]:
            if i.score < pivot.score:
                less_than.append(i)
            else:
                greater_than.append(i)

        return (cls.sort_by_descending_score(greater_than)
                + [pivot]
                + cls.sort_by_descending_score(less_than))



    # if (len(player_array) >= 2
    #         and player_array[0].score >= player_array[1].score):
    #     for i in range(len(player_array)):
    #         if player_array[i].score < player_array[i].score:
    #             break
    #     return player_array