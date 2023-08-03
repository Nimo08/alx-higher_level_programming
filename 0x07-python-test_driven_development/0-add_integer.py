#!/usr/bin/python3
"""
add_integer module
Calculates the sum of two numbers
Prints the sum to the stdout
"""


def add_integer(a, b=98):
    """
    Calculates the sum of two numbers:
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
