"""
Holds player information, and position
for the double linked player_list
"""

class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next = None
        self._pre = None

    def __str__(self):
        return f"Player Node for {self.player}"

    # <editor-fold desc="Properties and Setters">
    @property
    def key(self):
        return self.player.key

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, set_player):
        self._player = set_player

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, set_next):
        self._next = set_next

    @property
    def pre(self):
        return self._prev

    @pre.setter
    def pre(self, set_prev):
        self._prev = set_prev
    # </editor-fold>

