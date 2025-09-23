
from player_bst import PlayerBST

class PlayerBNode:

    def __init__(self, player: PlayerBST):
        self._player = player
        self._left = None
        self._right = None
    

    #Getters and Setters
    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, player: PlayerBST):
        self.left = player

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, player: PlayerBST):
        self.right = player