
"""
Testing possibilities for player hash map
"""

import unittest
from player_list import PlayerList
from player import Player
from player_node import PlayerNode
from app.player_hash_map import PlayerHashMap

class TestPlayerHashMap(unittest.TestCase):

    def setUp(self):
        self.test_hash_map = PlayerHashMap()

    def test_size_is_ten_on_init(self):
        self.assertEqual(len(self.test_hash_map.hash_map), 200, "Hash map is not equal to 10")

    def test_adds_a_player_node_by_hash(self):
        self.test_hash_map.__setitem__("001", "HashFriend")
        self.assertEqual(self.test_hash_map.__len__(), 1)

    def test_get_player_node(self):
        self.test_hash_map.__setitem__("001", "HashFriend")
        self.test_hash_map.__setitem__("002", "HashMutual")
        self.test_hash_map.__setitem__("003", "HashEnemy")
        self.test_hash_map.__setitem__("004", "HashLover")
        self.assertEqual(self.test_hash_map.__getitem__("003").player.name, "HashEnemy")
        self.assertEqual(self.test_hash_map.__len__(), 4)

    def test_delete_player_node_by_uid(self):
        self.test_hash_map.__setitem__("001", "HashFriend")
        self.test_hash_map.__setitem__("002", "HashMutual")
        self.test_hash_map.__delitem__("001")
        self.assertEqual(self.test_hash_map.__getitem__("001"), None)

    def test_display_hash(self):
        self.test_hash_map.__setitem__("001", "HashFriend")
        self.test_hash_map.__setitem__("002", "HashMutual")
        self.test_hash_map.__setitem__("003", "HashEnemy")
        self.test_hash_map.__setitem__("004", "HashLover")
        self.assertEqual(self.test_hash_map.__getitem__("003").player.name, "HashEnemy")

    def test_add_100_player_nodes(self):
        i = 1
        while i < 101:
            self.test_hash_map.__setitem__(str(i), "Hash_Player_" + str(i))
            i += 1
        self.assertEqual(self.test_hash_map.__getitem__("5").player.name, "Hash_Player_5")
        self.assertEqual(self.test_hash_map.__len__(), 100)
        print(self.test_hash_map.display())