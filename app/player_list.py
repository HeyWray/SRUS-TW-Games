
#Double linked list
class PlayerList(list):
    def __init__(self):
        self._root = None

    def __str__(self):
        return "List of Player"

    def push(self, player):
        self