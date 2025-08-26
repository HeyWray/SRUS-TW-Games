"""
Holds the player and where they are in
position to the double linked player_list
"""
from __future__ import annotations

class PlayerNode:
    def __init__(self, player):
        self._player = player #player
        self._next = None #the next player
        self._pre = None #the previous player

    def __str__(self):
        return f"Player Node for {self.player}"



    @property
    def key(self):
        return self.player.uid

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, set_to):
        self._player = set_to

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, set_to):
        self._next = set_to

    @property
    def pre(self):
        return self._pre

    @pre.setter
    def pre(self, set_to):
        self._pre = set_to

