#!/usr/bin/python3
"""
Shebang to create a PY script
"""


def rotate_2d_matrix(matrix):
    """method to rotate a matrix at 90 degree"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
