"""
A script that simply tests the linked list
and all the player components
"""

from app import player_list

list = player_list.PlayerList()

print("Is the list currently empty?", list.is_empty, "\n")
print("Adding 4 players \n")
list.push_to_front(player_list.new_player("001", "Chibi"))
list.push_to_front(player_list.new_player("002", "Zen"))
list.push_to_end(player_list.new_player("003", "Haruka"))
list.push_to_end(player_list.new_player())
list.push_to_front(player_list.new_player())
print("Checking again, is the list currently empty?", list.is_empty)
print("What is the list? ",list,"\n")

#test the end function
print("The end of the list is ", list.end.player.player_name)

print(list.contents)
print("\nThe end")


