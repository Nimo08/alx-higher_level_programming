#!/usr/bin/python3
"""
Module calls read_file function to read my_file_0.txt.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, 'r') as f:
        print(f.read())
