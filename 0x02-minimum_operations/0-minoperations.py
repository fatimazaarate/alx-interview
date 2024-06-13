#!/usr/bin/python3
"""function that calculates the min num of operations"""


def minOperations(n):
    """calculating the min num of operations
    to get a given num of chars"""

    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return 0
