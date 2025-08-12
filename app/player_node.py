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

    # <editor-fold desc="Properties and Setters">
    @property
    def key(self):
        #prefered to call player's UID but this
        #is an alternative call
        return self.player.uid

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, set):
        self._player = set

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, set):
        self._next = set

    @property
    def pre(self):
        return self._pre

    @pre.setter
    def pre(self, set):
        self._pre = set
    # </editor-fold>

