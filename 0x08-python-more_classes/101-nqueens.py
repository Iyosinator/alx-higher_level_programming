#!/usr/bin/python3
"""A program that solves the N-queens puzzle
"""
import sys


def is_safe(board, row, col):
    """Checks if a queen can be placed on board[row][col]
    without being threatened by other queens
    """
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            return False
    return True


def solve(board, col):
    """Solves the N-queens puzzle
    """
    n = len(board)
    if col == n:
        print(str([[i, board[i]] for i in range(n)]))
        return
    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve(board, col + 1)



if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0 for i in range(N)]
    solve(board, 0)
