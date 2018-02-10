import numpy as np


class Board:

    def __init__(self, rows, cols, n, position=None):
        self.rows = rows
        self.cols = cols
        self.n = n
        self.position = position if position is not None else np.zeros(rows * cols)
        self.size = self.position.size

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

    def winning(self):

        for p in range(0, self.rows * self.cols):
            vertical = 0
            horizontal = 0
            diagonal_down = 0
            diagonal_up = 0
            row = p // self.cols
            col = p % self.cols
            for i in range(0, self.n):
                if row + i < self.rows:
                    vertical += self.position[p + i]
                if col + i < self.cols:
                    horizontal += self.position[p + i * self.rows]
                if row + i < self.rows and col + i < self.cols:
                    diagonal_up += self.position[(p + i * (self.rows + 1))]
                if row - i >= 0 and col + i < self.cols:
                    diagonal_down += self.position[(p + i * (self.rows - 1))]
            if vertical == self.n:
                return 1
            if vertical == -1 * self.n:
                return -1
            if horizontal == self.n:
                return 1
            if horizontal == -1 * self.n:
                return -1
            if diagonal_down == self.n:
                return 1
            if vertical == -1 * self.n:
                return -1
            if diagonal_up == self.n:
                return 1
            if diagonal_up == -1 * self.n:
                return -1

        return 0


if __name__ == "__main__":
    board = Board(3, 3, 2)
    board.apply_move(0, -1).apply_move(1, 1)
    print(board.position)
    # print(board.winning())
    board.apply_move(0, -1).apply_move(1, 1)
    print(board.position)
    print(board.winning())
