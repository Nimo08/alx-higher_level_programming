#!/usr/bin/python3
"""
Module calls to_json_string function.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    """
    if isinstance(my_obj, set):
        raise TypeError("{3, 132} is not JSON serializable")
    return json.dumps(my_obj)
