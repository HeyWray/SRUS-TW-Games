"""
A script that simply tests the linked list
and all the player components
"""

from player_list import PlayerList
from player import Player
from player_node import PlayerNode

list = PlayerList()

def create_random_node():
    return PlayerNode(Player.from_random())

def player_in_node(uid, name):
    return PlayerNode(Player(uid, name))

print("Is the list currently empty?", list.is_empty, "\n")
print("Adding some players \n")

list.push_to_front(player_in_node("001", "Chibi"))
list.push_to_front(player_in_node("002", "Zen"))
list.push_to_end(PlayerNode(Player("003", "Haruka")))

print(list.root.key)

list.push_to_end(create_random_node())
list.push_to_front(create_random_node())

print("Checking again, is the list currently empty?", list.is_empty)
print("What is the list? ",list,"\n")

#test the last player node in the instanced player_list
print("The end of the list is ", list.end.player.player_name,"\n")

list.display(True)
list.display(False)

