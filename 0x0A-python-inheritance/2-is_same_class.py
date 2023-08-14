#!/usr/bin/python3
"""
Module checks if the object is exactly
an instance of the specified classes
Contains is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object
        a_class: class
    Returns True if the object is exactly
    an instance of the specified class ; otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
