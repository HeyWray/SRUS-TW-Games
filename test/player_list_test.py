"""
A script that simply tests the linked list
and all the player components
"""

import unittest
from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.player_list = PlayerList()

    def test_is_empty_list_on_start(self):
        self.assertIs(self.player_list.is_empty, True, "List is not empty on start")

    def test_push_to_front_adds_one_node(self):
        self.player_list.push_to_front(PlayerNode(Player("001", "Player1")))
        self.assertEqual(self.player_list.is_empty, False, "List has more then 1 node")

    def test_push_to_end_adds_one_node(self):
        self.player_list.push_to_end(PlayerNode(Player("001", "Player1")))
        self.assertEqual(len(self.player_list), 1, "List has more then 1 node")

    def test_random_player_is_added(self):
        self.player_list.push_to_front(PlayerNode(Player.create_random_player()))
        self.assertEqual(len(self.player_list), 1, "List has more then 1 node")

    def test_add_multiple_players(self):
        self.player_list.push_to_front(PlayerNode(Player("001", "Player1")))
        self.player_list.push_to_end(PlayerNode(Player("002", "Player2")))
        self.player_list.push_to_end(PlayerNode(Player("003", "Player3")))
        self.assertEqual(len(self.player_list), 3, "List has more then 3 player nodes")

    def test_push_to_front_is_in_correct_position(self):
        self.player_list.push_to_front(PlayerNode(Player("001", "Player1")))
        self.player_list.push_to_front(PlayerNode(Player("003", "Player1")))
        self.assertEqual(self.player_list.front.player.uid, "003", "List does not add to the front of the list")

    def test_push_to_end_is_in_correct_position(self):
        self.player_list.push_to_end(PlayerNode(Player("001", "Player1")))
        self.player_list.push_to_end(PlayerNode(Player("003", "Player1")))
        self.assertEqual(self.player_list.end.player.uid, "003", "List does not add to the end of the list")

    def test_remove_from_front(self):
        self.player_list.push_to_front(PlayerNode(Player("001", "Player1")))
        self.player_list.remove_from_front()
        self.assertEqual(self.player_list.is_empty, True, "List does not remove from front of list")

    def test_remove_from_end(self):
        self.player_list.push_to_front(PlayerNode(Player("001", "Player1")))
        self.player_list.remove_from_end()
        self.assertEqual(self.player_list.is_empty, True, "List does not remove from end of list")

    def test_remove_with_uid(self):
        self.player_list.push_to_front(PlayerNode(Player("001", "Player1")))
        self.player_list.remove_player_by_uid("001")
        self.assertEqual(self.player_list.is_empty, True, "List does not remove a UID of list")
