from Board import Board


class Game:

    def __init__(self, player, rows=6, cols=7, n=4, position=None):
        self.board = Board(rows, cols, n, position)
        self.player = player

    def play(self, player, col):
        # must be defined