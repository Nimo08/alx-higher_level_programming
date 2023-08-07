#!/usr/bin/python3


import sys


def nQueens(board=[[]], col=0, N=0):
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    if len(board) == col:
        print(board)
    else:
        for row in range(board):
            board[row][col] = 0
            row += 1
            if move_queen(board, row, col) is True:
                nQueens(board, col + 1)
            board[row][col] = "."


def move_queen(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
