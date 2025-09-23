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