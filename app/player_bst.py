
from player import Player
from player_bnode import PlayerBNode

class PlayerBST:

    def __init__(self):
        self._root = None

    def insert(self, player: Player,
               check_node: PlayerBNode | None = None):
        if self.root is None:
            self.root = PlayerBNode(player)
            return
        if check_node is None:
            check_node = self.root

        if check_node.player.name == player.name:
            self.update_player(check_node.player, player)
        elif check_node.player.name < player.name:
            if check_node.left is not None:
                self.insert(player, check_node.left)
            else:
                check_node.left = PlayerBNode(player)
        elif check_node.player.name >= player.name:
            if check_node.right is not None:
                self.insert(player, check_node.right)
            else:
                check_node.right = PlayerBNode(player)

    def update_player(self, old_player: Player, new_player: Player):
        old_player.name = new_player.name
        old_player.score = new_player.score
        old_player.uid = new_player.uid

    @classmethod
    def display(cls, node: PlayerBNode, indent: int = 1) -> str:
        message = ""
        if node.left is not None:
            message += cls.display(node.left, indent + 1)
        if node.right is not None:
            message += cls.display(node.right, indent + 1)
        str_indent = "  " * indent
        message = str(f"\n{str_indent}({indent - 1}) {node.player}") + message
        return message

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