"""
A script that simply tests the linked list
and all the player components
"""

import unittest
from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class test_player_list(unittest.TestCase):

    def test_is_empty_list_on_start(self):
        list = PlayerList()
        self.assertEqual(list.is_empty, True, "List is not empty on start")

    def test_push_to_front_adds_one_node(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player("001", "Player1")))
        self.assertEqual(list.is_empty, False, "List has more then 1 node")

    def test_push_to_end_adds_one_node(self):
        list = PlayerList()
        list.push_to_end(PlayerNode(Player("001", "Player1")))
        self.assertEqual(list.size, 1, "List has more then 1 node")

    def test_random_player_is_added(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player.create_random_player()))
        self.assertEqual(list.size, 1, "List has more then 1 node")

    def test_add_multiple_players(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player("001", "Player1")))
        list.push_to_end(PlayerNode(Player("002", "Player2")))
        list.push_to_end(PlayerNode(Player("003", "Player3")))
        self.assertEqual(list.size, 3, "List has more then 3 player nodes")

    def test_push_to_front_is_in_correct_position(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player("001", "Player1")))
        list.push_to_front(PlayerNode(Player("003", "Player1")))
        self.assertEqual(list.root.player.uid, "003", "List does not add to the front of the list")

    def test_push_to_end_is_in_correct_position(self):
        list = PlayerList()
        list.push_to_end(PlayerNode(Player("001", "Player1")))
        list.push_to_end(PlayerNode(Player("003", "Player1")))
        self.assertEqual(list.end.player.uid, "003", "List does not add to the end of the list")

    def test_remove_from_front(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player("001", "Player1")))
        list.remove_from_front()
        self.assertEqual(list.size, 0, "List does not remove from front of list")

    def test_remove_from_end(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player("001", "Player1")))
        list.remove_from_end()
        self.assertEqual(list.is_empty, True, "List does not remove from end of list")

    def test_remove_with_uid(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player("001", "Player1")))
        list.remove_uid("001")
        self.assertEqual(list.is_empty, True, "List does not remove a UID of list")

    def test_cant_remove_from_empty(self):
        list = PlayerList()
        list.push_to_front(PlayerNode(Player("001", "Player1")))
        print(list)
        list.remove_uid("001")
        #list.remove_from_front()
        self.assertEqual(list.is_empty, True, "List is empty")

    # def test_display(self):
    #     list = PlayerList()
    #     list.push_to_front(PlayerNode(Player("001", "Player1")))
    #     list.push_to_front(PlayerNode(Player("002", "Player2")))
    #     self.assertEqual(list.display(True), ("The list of players from front to back is:\n   ", list.root.player.__str__()),
    #     "List does not display the correct message from Front to Back")





# list = PlayerList()
#
# print("Is the list currently empty?", list.is_empty, "\n")
# print("Adding some players \n")
#
# list.push_to_front(PlayerNode(Player("001", "Chibi")))
# list.push_to_front(PlayerNode(Player("002", "Zen")))
# list.push_to_end(PlayerNode(Player("003", "Haruka")))
#
# print(list.root.key)
#
# list.push_to_end(PlayerNode(Player.from_random()))
# list.push_to_front(PlayerNode(Player.from_random()))
#
# print("Checking again, is the list currently empty?", list.is_empty)
# print("What is the list? ",list,"\n")
#
# #test the last player node in the instanced player_list
# print("The end of the list is ", list.end.player.player_name,"\n")
#
# print(list.display(True))
# print(list.display(False))