#!/usr/bin/python3
"""
Module calls append_write function.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    """
    with open(filename, 'a') as f:
        f.write(text)
        num_chars = len(text)
        return num_chars
