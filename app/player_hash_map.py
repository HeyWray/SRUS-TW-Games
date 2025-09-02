
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
        for _ in range(self.HASH_SIZE):
            self.hash_map.append(PlayerList())


    def __setitem__(self, key : str, value : str):
        """Add a new player to PlayerList in a
            corresponding index in the hash map.
            """
        uid = key
        name = value
        player_list = self.hash_map[self.get_index(uid)]
        player_list.push_to_end(PlayerNode(Player(uid, name)))


    def __getitem__(self, key : str) -> PlayerNode | None:
        """Retrieve a player from the PlayerList with
            the corresponding uid in the hash map.
            """
        uid = key
        player = self.hash_map[self.get_index(uid)].get_player_by_uid(uid)
        if player is not None:
            return self.hash_map[self.get_index(uid)].get_player_by_uid(uid)
        return None


    def __delitem__(self, key):
        """Remove a player from the PlayerList with
            the corresponding index in the hash map.
            """
        uid = key
        player_list = self.hash_map[self.get_index(uid)]
        if player_list.get_player_by_uid(uid) is not None:
            player_list.remove_player_by_uid(uid)

    def __len__(self) -> int:
        """Return the number of players in the hash map."""
        hash_size = 0
        for i in range(0, self.HASH_SIZE):
            hash_size += len(self.hash_map[i])
        return hash_size

    def display(self):
        display_message = "Displaying the Hash Map:\n"
        for i in range(0, self.HASH_SIZE):
            display_message += ("  Hash table " + str(i + 1) + " is length "
                                + str(len(self.hash_map[i])) + " with:\n   ")
            display_message += self.hash_map[i].display()
            display_message += "\n\n"
        return display_message

    def get_index(self, uid) -> int:
        return hash(uid) % self.HASH_SIZE
