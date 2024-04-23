#!/usr/bin/python3
"""
Rotates 2-D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates 2d matrix
    """
    size = len(matrix)
    for j in range(0, len(matrix) // 2 + 1):
        for i in range(j, size - 1):
            temp1 = matrix[i][size - 1]
            matrix[i][size - 1] = matrix[j][i]
            temp2 = matrix[size - 1][size - 1 - i + j]
            matrix[size - 1][size - 1 - i + j] = temp1
            temp1 = matrix[size - 1 - i + j][j]
            matrix[size - 1 - i + j][j] = temp2
            matrix[j][i] = temp1
        size -= 1
