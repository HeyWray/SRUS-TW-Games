
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
        while len(self.hash_map) < self.HASH_SIZE:
            self.hash_map.append(PlayerList())

    #Add a new player to PlayerList in a corresponding index in the hash map.
    def __setitem__(self, key, value):
        ...

    #Retrieve a player from the PlayerList with the corresponding index in the hash map.
    def __getitem__(self, item):
        ...

    #Remove a player from the PlayerList with the corresponding index in the hash map.
    def __delitem__(self, key):
        ...

    #Return the number of players in the hash map.
    def __len__(self):
        ...

    def sum_of_ascii_values(key: str, size: int) -> int:
        return sum(ord(char) for char in key) % size
