#!/usr/bin/python3
"""
Module calls save_to_json function.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        string = json.dumps(my_obj)
        return f.write(string)
