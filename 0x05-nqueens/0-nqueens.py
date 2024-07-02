#!/usr/bin/python3
"""
N-Queens Solver
"""

import sys

def is_safe(board, row, col, n):
    """
    Checks if placing a queen at (row, col) is safe.
    """
    for i in range(row):
        if board[i][col] == 1 or \
           board[i][col - row + i] == 1 or \
           board[i][col + row - i] == 1:
            return False
    return True

def find_all_solutions(board, row, n):
    """
    Finds all solutions for the N-Queens problem.
    """
    if row == n:
        return [[(i, j) for j in range(n) if board[i][j] == 1] for i in range(n)]

    solutions = []
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solutions.extend(find_all_solutions(board, row + 1, n))
            board[row][col] = 0

    return solutions

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = [[0 for _ in range(n)] for _ in range(n)]
    solutions = find_all_solutions(chessboard, 0, n)

    for solution in solutions:
        print(solution)
