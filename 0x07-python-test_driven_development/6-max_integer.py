#!/usr/bin/python3
"""
Module contains max_integer function
max_integer function: find and return max integer
in a list of integers
TypeError occurs when result is not an integer or a float
"""


def max_integer(list=[]):
    """
    Find and return the max integer in a list of integers
    If the list is empty, the function returns None
    Args:
        list: list
    Return: max integer in a list of integers
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
