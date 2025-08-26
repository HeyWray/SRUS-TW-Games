
"""
Testing possibilities for player hash map
"""

import unittest
from player_list import PlayerList
from player import Player
from player_node import PlayerNode
from player_hash_map import PlayerHashMap

class TestPlayerHashMap(unittest.TestCase):

    def setUp(self):
        self.test_hash_map = PlayerHashMap()

    def test_size_is_ten_on_init(self):
        self.assertEqual(len(self.test_hash_map.hash_map), 10, "Hash map is not equal to 10")