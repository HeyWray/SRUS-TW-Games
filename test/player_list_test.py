"""
A script that simply tests the linked list
and all the player components
"""

from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode

list = PlayerList()

print("Is the list currently empty?", list.is_empty, "\n")
print("Adding 2 players \n")
list.push(PlayerNode(Player("001", "Abigail")))
list.push(PlayerNode(Player("002", "Zen")))
print("Checking again, is the list currently empty?", list.is_empty)
print("What is the list? ",list,"\n")


