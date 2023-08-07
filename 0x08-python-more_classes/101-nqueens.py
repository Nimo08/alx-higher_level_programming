#!/usr/bin/python3


import sys


def nQueens(self, n) -> list[list[str]]:
    """Solves the N queens problem"""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = int(sys.argv[1])
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    cols = set()
    posDiagonals = set()
    negDiagonals = set()

    res = []
    for i in range(n):
        board = [["."]]

    def backtrack(row):
        if row == n:
            board_copy = []
            for row in board:
                board_copy += ".".join(row)
            res.append(board_copy)
            return
        for col in range(n):
            if col in cols or (row + col) in posDiagonals \
                    or (row - col) in negDiagonals:
                continue
            cols.add(col)
            negDiagonals.add(row - col)
            posDiagonals.add(row + col)
            board[row][col] = "Q"

            backtrack(row + 1)

            cols.remove(col)
            negDiagonals.remove(row - col)
            posDiagonals.remove(row + col)
            board[row][col] = "."
    backtrack(0)
    return res
