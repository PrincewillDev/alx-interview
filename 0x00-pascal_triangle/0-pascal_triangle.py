#!/usr/bin/python3
"""
Returns a list of integers representing the Pascal's triangle
"""

def pascal_triangle(n):
    """ Fnction returns a list of integers representing Pascal's Triangle
    Args:
        n(int): Number of triangle rows to print
    Return:
        list of lists: List of integers of triangle organized into rows
    """
    if n <= 0:
        return[]

    result = [[1]]

    for i in range(n - 1):
        temp = [0] + result[-1] + [0]
        row = []

        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)
    return result
