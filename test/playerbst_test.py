
import unittest
import random
from player import Player
from player_bst import PlayerBST

class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.names = ["Olivia", "Emma", "Amelia", "Charlotte", "Mia", "Sophia", "Isabella", "Evelyn", "Ava", "Sofia", "Liam", "Noah", "Oliver", "Theodore", "James", "Henry", "Mateo", "Elijah", "Lucas", "William"]
        self.bst = PlayerBST()

    def test_insert_on_root(self):
        self.assertIs(self.bst.is_empty, True, "Tree is not empty on start")

    def test_insert_on_root(self):
        self.bst.insert(Player("001", random.choice(self.names)))
        self.assertIs(self.bst.is_empty, False)

    def test_add_10_to_bst(self):
        i = 1
        for i in range(1, 11):
            self.bst.insert(Player(f"00{i}", random.choice(self.names)))
        self.assertEqual(i, 10)