#!/usr/bin/python3
"""
Module illustrates the use of try, except
to add a new attribute to an object.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
