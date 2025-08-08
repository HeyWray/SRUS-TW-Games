"""
Holds the list of all players
"""
from __future__ import annotations
import random
from tkinter import BooleanVar

from app.player_node import PlayerNode
from app.player import Player


# Double linked list
class PlayerList(list):
    def __init__(self):
        self._root = None
        self._current = None
        self._end = None

    def __str__(self):
        return f"Double link List of Players of size {self.size}"

    # Adds a new player at the START of the list
    # if the list is empty will just make a list of 1
    def push_to_front(self, player: PlayerNode):
        if type(player) is not PlayerNode:
            raise ValueError("Error: You need to pass a PlayerNode. "
                             "See new_player in app.player_list")
        if self.root is None:
            self.root = player
            self.end = player
            return
        self.root.pre = player
        player.next = self.root
        self.root = player

    # Adds a new player at the END of the list
    # if the list is empty will just make a list of 1
    def push_to_end(self, player: PlayerNode):
        if type(player) is not PlayerNode:
            raise ValueError("Error: You need to pass a PlayerNode. "
                             "See new_player in app.player_list")
        if self.end is None:
            self.root = player
            self.end = player
            return
        self.end.next = player
        player.pre = self.end
        self.end = player

    # Removes whoever the front player is
    def remove_from_front(self):
        if self.root is None:
            return
        if self.root == self.end:
            self.root = None
            self.end = None
            return
        self.root = self.root.next
        self.root.pre = None

    # Removes whoever the end player is
    def remove_from_end(self):
        if self.end is None:
            return
        if self.root == self.end:
            self.root = None
            self.end = None
            return
        self.end = self.end.pre
        self.end.next = None

    #Removes a player based on a uid
    def remove_uid(self, uid: str):
        if self.root is None:
            return
        check_player = self.root
        while check_player.player.uid != uid:
            check_player = check_player.next
            if check_player is None:
                raise ValueError("WARNING! Could not find player with uid ", uid,
                      " (app.player_list in def remove_uid)")
        #we found the uid

        #is it the only one in the link?
        if self.size <= 1:
            self.root = None
            self.end = None
            return
        #is the link at the start or the end?
        if (check_player == self.root or
            check_player == self.end):
            if check_player == self.root:
                self.root = check_player.next
                self.root.pre = None
            if check_player == self.end:
                self.end = check_player.pre
                check_player.next = None
            return

        #else it is somewhere through the chain
        check_player.pre.next = check_player.next
        check_player.next.pre = check_player.pre

    # Lists out the player names in order
    def display(self, forward=True):
        display = "The list of players from front to back is:\n   "
        link = self.root
        if not forward:
            display = "The list of players from back to front is:\n   "
            link = self.end
        while link is not None:
            display += link.player.__str__()
            if link.next is None and forward:
                break
            elif link.pre is None and not forward:
                break
            display += "\n   "
            if forward:
                link = link.next
            else:
                link = link.pre
        print(display)

    # <editor-fold desc="Properties and Setters">

    # is the list empty?
    @property
    def is_empty(self):
        if self.root is None:
            return True
        return False

    # How big the list is
    @property
    def size(self) -> int:
        if self.root is None:
            return 0
        count: int = 1
        n = self.root
        while n.next is not None:
            n = n.next
            count += 1
        return count

    # Start of the list
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    # End of the list
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    # </editor-fold>


# Static. Handles creating a new player. If no name or uid
# is specified then creates a random name and uid
def new_player(uid: str | None = None,
               name: str | None = None) -> PlayerNode:
    new_uid = uid
    new_name = name
    if uid is None:
        new_uid = str(random.randrange(
            100, 1000))
    if name is None:
        new_name = random.choice(
            list(["Nagz", "Ray", "Bluto", "Heavenly"]))
    return PlayerNode(Player(new_uid, new_name))
