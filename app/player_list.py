"""
Holds the list of all players
"""
from __future__ import annotations

from player_node import PlayerNode


# Player linked list
class PlayerList:
    def __init__(self):
        self._front = None
        self._current = None
        self._end = None

    def __str__(self):
        return f"Player link List of Players of size {len(self)}"

    def __repr__(self):
        return f"Player link List of Players of size {len(self)!r}"

    def __len__(self) -> int:
        """How big the list is"""
        if self.front is None:
            return 0
        count: int = 1
        n = self.front
        while n.next is not None:
            n = n.next
            count += 1
        return count

    def push_to_front(self, player: PlayerNode):
        """Adds a new player at the START of the list
            if the list is empty will just make a list of 1
            """
        if not isinstance(player, PlayerNode):
            raise TypeError("Error: You need to pass a PlayerNode. "
                             "See new_player in app.player_list")
        if self.is_empty:
            self.front = player
            self.end = player
            return
        self.front.pre = player
        player.next = self.front
        self.front = player

    def push_to_end(self, player: PlayerNode):
        """Adds a new player at the END of the list
            if the list is empty will just make a list of 1
            """
        if not isinstance(player, PlayerNode):
            raise TypeError("Error: You need to pass a PlayerNode. "
                             "See new_player in app.player_list")
        if self.is_empty:
            self.front = player
            self.end = player
            return
        self.end.next = player
        player.pre = self.end
        self.end = player

    def remove_from_front(self):
        """Removes whoever the front player is"""
        if self.front == self.end:
            self.front = None
            self.end = None
            return
        self.front = self.front.next
        self.front.pre = None

    def remove_from_end(self):
        """Removes whoever the end player is"""
        if self.front == self.end:
            self.front = None
            self.end = None
            return
        self.end = self.end.pre
        self.end.next = None

    def remove_player_by_uid(self, uid: str):
        """Removes a player based on a uid"""
        if len(self) == 0:
            raise ValueError(("Error: The list is empty. Size is ", len(self)), self)
        check_player = self.front
        while check_player.player.uid != uid:
            check_player = check_player.next
            if check_player is None:
                raise ValueError("WARNING! Could not find player with uid ", uid,
                      " (app.player_list in def remove_uid)")
        #we found the uid

        #is it the only one in the link?
        if len(self) <= 1:
            self.front = None
            self.end = None
            return

        #else it is somewhere through the chain
        check_player.pre.next = check_player.next
        check_player.next.pre = check_player.pre


    def display(self, forward=True) -> str:
        """Returns a list of player names in order
            true for front to end, false for end to front
            """
        display = "The list of players from front to back is:\n   "
        link = self.front
        if not forward:
            display = "The list of players from back to front is:\n   "
            link = self.end
        while link is not None:
            display += str(link.player)
            if link.next is None and forward:
                break
            elif link.pre is None and not forward:
                break
            display += "\n   "
            if forward:
                link = link.next
            else:
                link = link.pre
        return display


    @property
    def is_empty(self):
        """Is the list empty?"""
        return self.front is None

    @property
    def front(self):
        """Start of the list"""
        return self._front

    @front.setter
    def front(self, value):
        self._front = value

    @property
    def end(self):
        """End of the list"""
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

