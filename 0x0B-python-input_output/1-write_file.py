#!/usr/bin/python3
"""
Module calls write_file function to write to a
text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    and returns the number of characters written:
    """
    filename = "my_first_file.txt"
    text = "This School is so cool!\n"
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
