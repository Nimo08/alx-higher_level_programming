#!/usr/bin/python3
"""
Module calls class_to_json function.
"""


def class_to_json(obj):
    """
    Returns dictionary description for JSON
    serialization of an object.
    """
    dict_1 = obj.__dict__
    return dict_1
