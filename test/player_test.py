#short test for player

import unittest
from player_list import PlayerList
from player import Player
from player_node import PlayerNode

class test_player(unittest.TestCase):
    def test_player_uid(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player("002", "Player2")))
        self.assertEqual(list.root.player.uid, "002", "List does not have the correct UID (at front)")
        self.assertEqual(list.end.player.uid, "002", "List does not have the correct UID (at end)")


    def test_player_name(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player("003", "Player3")))
        self.assertEqual(list.root.player.name, "Player3", "List does not have the correct name (at front)")
        self.assertEqual(list.end.player.name, "Player3", "List does not have the correct name (at end)")