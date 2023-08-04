#!/usr/bin/python3
"""
Module contains print_square function
print_square function: prints a square made of # to stdout
TypeError occurs when size is not equal to or larger than 0
TypeError occurs when size is not an integer
"""


def print_square(size):
    """
    Prints a square made of # to stdout.
    Args:
        size: integer
    Return: square made of #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
