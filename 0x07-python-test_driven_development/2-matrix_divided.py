#!/usr/bin/python3
"""
matrix_divided module
Divides all elements of a matrix
Prints the result to stdout
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list):
        raise TypeError(matrix_error)
    for row in matrix:
        if not isinstance(row, (list)):
            raise TypeError(matrix_error)
        if len(row) != len(matrix[0]):
            raise TypeError(len_error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    res = list(map(lambda row: list(map(lambda x: round(x / div, 2), row)),
                   matrix))
    return res
