#!/usr/bin/python3
"""
say_my_name module
Checks if name is string
Prints first and last name to stdout.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name to stdout.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    first_name = first_name.strip()
    last_name = last_name.strip()
    if first_name and last_name:
        print("My name is {} {}".format(first_name, last_name))
    elif first_name:
        print("My name is {}".format(first_name))
    else:
        print("My name is")
