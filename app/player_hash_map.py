
"""
Hash map for the player, holds a series of player lists
"""

from player_list import PlayerList
from player import Player
from player_node import PlayerNode

class PlayerHashMap():

    HASH_SIZE: int = 10

    def __init__(self):
        self.hash_map = []
        for _ in range(self.HASH_SIZE):
            self.hash_map.append(PlayerList())

    def __setitem__(self, uid : str, name : str):
        """Add a new player to PlayerList in a
            corresponding index in the hash map.
            """
        player_list = self.hash_map[self._hash_of_uid(uid)]
        player_list.push_to_end()

    def __getitem__(self, uid : str) -> PlayerNode | None:
        """Retrieve a player from the PlayerList with
            the corresponding uid in the hash map.
            """
        player = self.hash_map[self._hash_of_uid(uid)].get_player_by_uid(uid)
        if player is None:
            raise ValueError(f"Cannot get player {uid}")
        return player


    def __delitem__(self, uid):
        """Remove a player from the PlayerList with
            the corresponding index in the hash map.
            """
        player_list = self.hash_map[self._hash_of_uid(uid)]
        if player_list is None:
            raise Exception(f"Trying to delete player {uid} that doesn't exist")
        player_list.remove_player_by_uid(uid)

    def __len__(self) -> int:
        hash_size = 0
        for i in range(0, self.HASH_SIZE):
            hash_size += len(self.hash_map[i])
        return hash_size

    def display(self):
        """Prints a large message of every
        player_list and each list's contents
        """
        display_message = "Displaying the Hash Map:\n"
        for i in range(0, self.HASH_SIZE):
            display_message += ("  Hash table " + str(i + 1) + " is length "
                                + str(len(self.hash_map[i])) + " with:\n   ")
            display_message += self.hash_map[i].display()
            display_message += "\n\n"
        return display_message

    def _hash_of_uid(self, uid) -> int:
        """Get the hash value of a given player uid"""
        return Player.hash_method(uid) % self.HASH_SIZE
