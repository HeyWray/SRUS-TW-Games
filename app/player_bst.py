from operator import truediv
from tkinter import BooleanVar

from player import Player
from player_bnode import PlayerBNode

class PlayerBST:
    """
    Player Binary Search Tree.
    Holds a series of PlayerBNodes containing Players in a binary tree form.
    """

    def __init__(self):
        self._root = None

    def __str__(self):
        return f"PlayerBST of length {self.size()} and a root of {self.root}"

    def __len__(self):
        return self.size()

    def insert(self, player: Player, check_node: PlayerBNode | None = None):
        """
        Creates a new PlayerBNode with player
        and inserts it into the PlayerBST.

        :param player:
        :param check_node: If unspecified, will start at root
        :return:
        """

        #If the tree is empty, start the tree with the player
        if self.root is None:
            self.root = PlayerBNode(player)
            return

        #Start search from root if None
        if check_node is None:
            check_node = self.root

        #If they have the same name then update the player
        if check_node.player.name == player.name:
            self._update_player(check_node.player, player)
        #If the player is greater than put it in the right
        elif check_node.player.name < player.name:
            if check_node.right is not None:
                self.insert(player, check_node.right)
            else:
                check_node.right = PlayerBNode(player)
        # If the player is lesser than put it in the left
        elif check_node.player.name >= player.name:
            if check_node.left is not None:
                self.insert(player, check_node.left)
            else:
                check_node.left = PlayerBNode(player)

    def search(self, player_name: str) -> PlayerBNode | None:
        """
        Searches a PlayerBST for a player by a specific name.
        Returns the PlayerBNode or None.
        :param player_name: Player name to search for
        :return:
        """
        # If the tree is empty return None
        if self.root is None:
            return None

        check_node = self.root
        #while loop. compare each child recursively till you find the player or none
        while True:
            if (check_node is None or
                    check_node.player.name == player_name):
                return check_node
            elif (check_node.right is not None
                  and check_node.player.name < player_name):
                check_node = check_node.right
            elif (check_node.left is not None
                  and check_node.player.name > player_name):
                check_node = check_node.left
            else:
                return None

    def _update_player(self, old_player: Player, new_player: Player):
        old_player.name = new_player.name
        old_player.score = new_player.score
        old_player.uid = new_player.uid

    def sort(self, set_node : PlayerBNode | None = None, bst_array : [PlayerBNode] = [] ):
        """
        Sorts the PlayerBST and re-balances it
        :param set_node: Used internally to set left and right nodes
        :param bst_array: User internally to sequentially divide a sorted arrayed version of the BST
        :return:
        """
        if self.root is None:
            return

        #first time around, get BST as array, sorts it, and assign middle as root
        if set_node is None:
            bst_array = self.get_as_array()
            bst_array = sorted(bst_array)
            self.root = bst_array.pop(len(bst_array)//2)
            set_node = self.root

        #subsequent recursions
        else:
            #find the center of the array
            middle = bst_array.pop(len(bst_array)//2)
            #assign the right or left if it is bigger
            if set_node < middle:
                set_node.right = middle
            else:
                set_node.left = middle
            set_node = middle

        #clear the node's previous children
        set_node.left = None
        set_node.right = None

        # split the array into 2
        left_split = bst_array[:len(bst_array)//2]
        right_split = bst_array[len(bst_array) // 2:]

        #if either split has nodes then start another recursion
        if len(left_split) > 0:
            self.sort(set_node, left_split)
        if len(right_split) > 0:
            self.sort(set_node, right_split)

    def get_as_array(self, player_b_node : PlayerBNode | None = None) -> []:
        #start at root
        if player_b_node is None:
            player_b_node = self.root

        bst_array = []

        bst_array.append(player_b_node)

        if player_b_node.left is not None:
            bst_array += self.get_as_array(player_b_node.left)

        if player_b_node.right is not None:
            bst_array += self.get_as_array(player_b_node.right)

        return bst_array

    def display(self, player_b_node: PlayerBNode | None = None, indent: int = 1) -> str:
        """
        Returns a string of the whole PlayerBST with indents in the debugger.
        Remember to print the result.
        :param player_b_node:
        :param indent:
        :return:
        """

        #start at root
        if player_b_node is None:
            player_b_node = self.root
        #create an empty message
        message = ""
        #recursively add string messages of Player __str__ information
        if player_b_node.left is not None:
            message += self.display(player_b_node.left, indent + 1)
        if player_b_node.right is not None:
            message += self.display(player_b_node.right, indent + 1)
        #add spaces for indentation to make the print more legible
        str_indent = "  " * indent
        #construct the message
        message = str(f"\n{str_indent}({indent - 1}) {player_b_node.player}") + message
        return message

    def size(self, check_node : PlayerBNode | None = None,
             size: int = 0) -> int:
        if self.root is None:
            return 0
        if check_node is None:
            check_node = self.root

        size += 1
        if check_node.left is not None:
            size += self.size(check_node.left)
        if check_node.right is not None:
            size += self.size(check_node.right)
        return size


    ##Getters and Setters
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node: PlayerBNode):
        self._root = node

    @property
    def is_empty(self):
        return self.root is None
