#!/usr/bin/python3
"""
Module calls pascal_triangle function.
"""


def factorial(x):
    """
    Computes factorial of a number.
    """
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def pascal_triangle(n):
    """
    Returns a list of integers representing
    the Pascal's triangle of n.
    """
    res = []
    if n <= 0:
        return res
    for i in range(n):
        row = []
        for j in range(i+1):
            ans = factorial(i) // (factorial(j) * factorial(i-j))
            row.append(ans)
        res.append(row)
    return res
