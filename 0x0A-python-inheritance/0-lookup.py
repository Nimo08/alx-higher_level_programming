#!/usr/bin/python3
"""
Module contains two classes: MyClass1 which is empty,
and MyClass2 which contains an attribute and a function
It also contains the lookup function which returns
the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj: object
    Return:
        list
    """
    return dir(obj)
