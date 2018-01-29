import copy
import numpy as np

class Board:

    def __init__(self, rows, cols, n, board=None):
        self.rows = rows
        self.cols = cols
        self.n = n
        self.board = board if board is not None else np.zeros((rows,cols))

    def apply_move(self, col, player):

        i = -1
        for r in range(self.rows):
            if self.board[r][col] == 0:
                i = r
                break

        if i == -1:
            raise ValueError('Board is full at this column')

        self.board[i][col] = player

        return self


if __name__ == "__main__":
    board = Board(3, 3, 2)
    print(board.board)
    board.apply_move(0,1)
    print(board.board)
    board.apply_move(0,1)
    print(board.board)
    board.apply_move(0,1)
    print(board.board)
    board.apply_move(0,1)
    print(board.board)
