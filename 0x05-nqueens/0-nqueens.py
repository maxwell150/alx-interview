#!/usr/bin/python3
"""challenge of placing N non-attacking queens on an N×N chessboard
"""
import sys


def safe_position(board, n, i):
    """checks a place is not attacked by queens
    """
    for j in range(n):
        if(board[j] == i or board[j] + n - j == i or board[j] + j - n == i):
            return False
    return True


def create_board(board, n):
    """finds the next safe posn to land the queen
    """
    for i in range(len(board)):
        if safe_position(board, n, i):
            board[n] = i
            if n < len(board) - 1:
                create_board(board, n + 1)
            else:
                print([[i, board[i]] for i in range(len(board))])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
board = [-1 for i in range(n)]
create_board(board, 0)
