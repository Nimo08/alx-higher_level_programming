#!/usr/bin/python3
"""
max_integer module
Module to find the max integer in a list
Prints the max_integer to stdout
"""


def max_integer(list=[]):
    """
    Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    if not isinstance(result, (int, float)):
        raise TypeError("result must be an integer")
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
