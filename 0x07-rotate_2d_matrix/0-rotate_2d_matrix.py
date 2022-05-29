#!/usr/bin/python3
"""rotate a 2 d matrix clockwise
"""


def rotate_2d_matrix(matrix):
    """rotate
    """
    first = 0
    nrow = len(matrix) - 1
    while first < nrow:
        for x in range(first, nrow):
            temp = matrix[x][nrow]
            matrix[x][nrow] = matrix[first][x]
            temp1 = matrix[nrow][nrow + first - x]
            matrix[nrow][nrow + first - x] = temp
            temp = matrix[nrow + first - x][first]
            matrix[nrow + first - x][first] = temp1
            matrix[first][x] = temp
        first += 1
        nrow -= 1
