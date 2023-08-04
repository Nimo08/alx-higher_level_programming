#!/usr/bin/python3
"""
Module contains add_integer function
add_integer function: calculates sum of two numbers
and prints the result to stdout
TypeError occurs when a is not an integer
TypeError occurs when b is not an integer
"""


def add_integer(a, b=98):
    """
    Calculates the sum of two numbers: a and b
    Args:
        a: integer
        b: integer
    Return: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    return a + b
