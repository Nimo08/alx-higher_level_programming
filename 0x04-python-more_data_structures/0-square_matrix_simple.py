#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = list(map(lambda row: [i ** 2 for i in row], matrix))
    return squared
