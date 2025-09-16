#short test for player

import unittest
from player_list import PlayerList
from player import Player
from player_node import PlayerNode

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("001", "Thomas")

    def test_player_uid(self):
        player_list = PlayerList()
        player_list.push_to_front(PlayerNode(Player("002", "Player2")))
        self.assertEqual(player_list.front.player.uid, "002", "List does not have the correct UID (at front)")
        self.assertEqual(player_list.end.player.uid, "002", "List does not have the correct UID (at end)")


    def test_player_name(self):
        player_list = PlayerList()
        player_list.push_to_front(PlayerNode(Player("003", "Player3")))
        self.assertEqual(player_list.front.player.name, "Player3", "List does not have the correct name (at front)")
        self.assertEqual(player_list.end.player.name, "Player3", "List does not have the correct name (at end)")

    def test_sort_players(self):
        players = [Player("001", "Alice", 10), Player("002", "Bob",5),
                   Player("003", "Charlie", 15)]
        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player("002","Bob", 5), Player("001", "Alice", 10),
                                   Player("003", "Charlie", 15)]

        print(f"sorted = {sorted_players},\nmanual = {manually_sorted_players}")

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player("001", "Alice", 10)
        bob = Player("002", "Bob", 5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(bob < alice)
        # or, event better
        self.assertGreater(alice, bob)