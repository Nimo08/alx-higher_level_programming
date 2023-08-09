#!/usr/bin/python3


import sys


def nQueens(N):
    cols = set()
    posDiagonals = set()
    negDiagonals = set()

    board = []

    def backtrack(rows):
        if rows == int(sys.argv[1]):
            print(board)
            return

        for c in range(int(sys.argv[1])):
            if c in cols or (rows + c) in posDiagonals \
                    or (rows - c) in negDiagonals:
                continue

            cols.add(c)
            posDiagonals.add(rows + c)
            negDiagonals.add(rows - c)
            board.append([rows, c])

            backtrack(rows + 1)

            cols.remove(c)
            posDiagonals.remove(rows + c)
            negDiagonals.remove(rows - c)
            board.remove([rows, c])

    backtrack(0)


nQueens(int(sys.argv[1]))
