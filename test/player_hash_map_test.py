
"""
Testing possibilities for player hash map
"""

import unittest
from player_hash_map import PlayerHashMap

class TestPlayerHashMap(unittest.TestCase):

    def setUp(self):
        self.test_hash_map = PlayerHashMap()

    def test_size_is_ten_on_init(self):
        self.assertEqual(len(self.test_hash_map.hash_map), 10, "Hash map is not equal to 10")

    def test_adds_a_player_node_by_hash(self):
        self.test_hash_map["001"] = "HashFriend"
        self.assertEqual(len(self.test_hash_map), 1)

    def test_get_player_node(self):
        self.test_hash_map["001"] = "HashFriend"
        self.test_hash_map["002"] = "HashMutual"
        self.test_hash_map["003"] = "HashEnemy"
        self.test_hash_map["004"] = "HashLover"
        self.assertEqual(self.test_hash_map["003"].player.name, "HashEnemy")
        self.assertEqual(len(self.test_hash_map), 4)

    def test_delete_player_node_by_uid(self):
        self.test_hash_map["001"] = "HashFriend"
        self.test_hash_map["002"] = "HashMutual"
        del self.test_hash_map["001"]
        self.assertEqual(self.test_hash_map["001"], None)

    def test_delete_on_an_empty_hash(self):
        del self.test_hash_map["001"]
        self.assertEqual(self.test_hash_map["001"], None)
        self.test_hash_map["001"] = "HashFriend"
        del self.test_hash_map["001"]
        del self.test_hash_map["001"]
        self.assertEqual(self.test_hash_map["001"], None)

    def test_display_hash(self):
        self.test_hash_map["001"] = "HashFriend"
        self.test_hash_map["002"] = "HashMutual"
        self.test_hash_map["003"] = "HashEnemy"
        self.test_hash_map["004"] = "HashLover"
        self.assertEqual(self.test_hash_map["003"].player.name, "HashEnemy")

    def test_add_100_player_nodes(self):
        for i in range (1,101):
            self.test_hash_map[str(i)] = "Hash_Player_" + str(i)
        self.assertEqual(self.test_hash_map["5"].player.name, "Hash_Player_5")
        self.assertEqual(len(self.test_hash_map), 100)
        print(self.test_hash_map.display())