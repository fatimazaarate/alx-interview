#!/usr/bin/python3
"""a pascal triangle"""


def pascal_triangle(n):
    """ function that returns a list of lists of integers
         representing the Pascal’s triangle of n"""

     if n <= 0:
        return []
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            old_row = triangle[i - 1]
            new_row = [1]
            new_row.extend(
                [
                    old_row[j] + old_row[j + 1]
                    for j in range(len(old_row) - 1)
                ]
            )
            new_row.append(1)
            triangle.append(new_row)
    return triangle

