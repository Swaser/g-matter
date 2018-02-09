import numpy as np


class Board:

    def __init__(self, rows, cols, n, position=None):
        self.rows = rows
        self.cols = cols
        self.n = n
        self.position = position if position is not None else np.zeros(rows * cols)

    def apply_move(self, col, player):

        if not (player == 1 or player == -1):
            raise ValueError('Player must be 1 or -1')

        for p in range(col * self.rows,
                       (col + 1) * self.rows):
            if self.position[p] == 0:
                self.position[p] = player
                break
            if p == (col + 1) * self.rows - 1:
                raise ValueError('Column full')

        return self

    def is_winning(self, player):

        return False


if __name__ == "__main__":
    board = Board(3, 3, 2)
