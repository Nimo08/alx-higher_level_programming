#!/usr/bin/python3
"""
Module calls load_from_json_file function.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file."
    """
    with open(filename, 'r') as f:
        obj = json.load(f)
        return obj
