#!/usr/bin/python3
"""This is a module to calculate the perimeter of islands.
"""


def island_perimeter(grid):
    """This function calculates the perimeter of islands.

    Args:
        grid (list): 2D array matrix of 0s and 1s.

    Returns:
        int: The perimeter of the islands.
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    return perimeter
