#!/usr/bin/python3
"""
Module contains matrix_divided function
matrix_divided function: divides all elements of a matrix
and prints the result to stdout
TypeError occurs when matrix is not a (list of lists) of integers/floats
TypeError occurs when each row of the matrix is not of the same size
TypeError occurs when div is not an integer or float
ZeroDivisionError occurs when div is not equal to 0
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    Args:
        matrix: list of lists
        div: integer
    Return: result of division
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
