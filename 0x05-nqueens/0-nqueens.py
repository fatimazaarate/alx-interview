#!/usr/bin/python3
"""solving the n queen problem"""

import sys


def safe(board, row, col):
    """checking if a queen is safe to be placed at board[row][col] """
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n):
    """using backtracking to solve nqueen prob"""
    solutions = []

    def backtrack(board, row):
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return
        for col in range(n):
            if safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    board = [-1] * n
    backtrack(board, 0)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
