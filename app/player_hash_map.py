
"""
Hash map for the player, holds a series of player lists
"""

from player_list import PlayerList
from player import Player
from player_node import PlayerNode

class PlayerHashMap():

    HASH_SIZE: int = 200

    def __init__(self):
        self.hash_map = []
        while len(self.hash_map) < self.HASH_SIZE:
            self.hash_map.append(PlayerList())

    """Add a new player to PlayerList in a 
    corresponding index in the hash map.
    """
    def __setitem__(self, uid : str, name : str):
        player_list = self.hash_map[self.get_index(uid)]
        # if (player_list.__len__ != 0
        #         and player_list.get_player_by_uid(uid) is not None):
        #     player_list.push_to_end(uid, name)
        # else:
        player_list.push_to_end(PlayerNode(Player(uid, name)))

    """Retrieve a player from the PlayerList with 
    the corresponding uid in the hash map.
    """
    def __getitem__(self, uid : str) -> PlayerNode | None:
        player = self.hash_map[self.get_index(uid)].get_player_by_uid(uid)
        if player is not None:
            return self.hash_map[self.get_index(uid)].get_player_by_uid(uid)
        return None

    """Remove a player from the PlayerList with 
    the corresponding index in the hash map.
    """
    def __delitem__(self, uid):
        player_list = self.hash_map[self.get_index(uid)]
        if player_list.get_player_by_uid(uid) is not None:
            player_list.remove_player_by_uid(uid)

    """Return the number of players in the hash map."""
    def __len__(self) -> int:
        hash_size = 0
        i = 0
        while i < self.HASH_SIZE:
            hash_size += self.hash_map[i].__len__
            i += 1
        return hash_size

    def display(self):
        display_message = ""
        i = 0
        while i < self.HASH_SIZE:
            display_message += ("Hash table " + str(i + 1) + " is length "
                                + str(self.hash_map[i].__len__) + " with:\n   ")
            display_message += self.hash_map[i].display()
            display_message += "\n\n"
            i += 1
        return display_message

    def get_index(self, uid) -> int:
        return hash(uid) % self.HASH_SIZE

    # def sum_of_ascii_values(key: str, size: int) -> int:
    #     return sum(ord(char) for char in key) % size