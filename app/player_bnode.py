import random

from player import Player

class PlayerBNode:
    """
    Individual nodes of Players for the player_bst (Player Binary Search Tree)
    """
    def __init__(self, player: Player):
        self._player = player
        self._player.score = random.randint(1, 1000)
        self._left = None
        self._right = None

    def __str__(self):
        return f"PlayerBNode of Player {self.player.name}, score: {self.player.score}"

    def __lt__(self, other):
        return self.player.name < other.player.name

    def __ge__(self, other):
        return self.player.name > other.player.name

    #Getters and Setters
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, new_player):
        self._player = new_player

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, player):
        self._left = player

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, player):
        self._right = player