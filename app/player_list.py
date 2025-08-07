"""
Holds the list of all players
"""

from app.player_node import PlayerNode

#Double linked list
class PlayerList(list):
    def __init__(self):
        self._root = None
        self._current = None
        self._end = None

    def __str__(self):
        return f"Double link List of Players of size {self.size}"



    #Adds a new player at the head of the list
    #if the list is empty will just make a list of 1
    def push(self, player):
        if self.root is None:
            self.root = player
            self.end = player
            return
        new_player = PlayerNode(player)
        self.root.pre = new_player
        new_player.next = self.root
        self.root = new_player



    # <editor-fold desc="Properties and Setters">

    #is the list empty?
    @property
    def is_empty(self):
        if self.root is None:
            return True
        return False

    #How big the list is
    @property
    def size(self) -> int:
        if self.root is None:
            return 0
        count : int = 1
        n = self.root
        while n.next is not None:
            n = n.next
            count += 1
        return count

    #Begining of the list
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    #End of the list
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    # </editor-fold>