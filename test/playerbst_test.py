
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
        for i in range(1, 11):
            self.bst.insert(Player(f"00{i}", f"{random.choice(self.names)} {i}"))
        self.assertEqual(len(self.bst), 10)

    def test_search(self):
        for i in range(1, 11):
            self.bst.insert(Player(f"00{i}", f"{random.choice(self.names)} {i}"))
        self.bst.insert(Player(f"011", "Billy Bob"))
        self.assertIsNotNone(self.bst.search("Billy Bob"))
        self.assertEqual(self.bst.search("Billy Bob").player.name, "Billy Bob")

    def test_sort(self):
        for i in range(1, 11):
            self.bst.insert(Player(f"00{i}", f"{random.choice(self.names)} {i}"))
        self.bst.sort()