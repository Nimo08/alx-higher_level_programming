#!/usr/bin/python3
"""
Module contains say_my_name function
say_my_name function: checks if name is string
and prints first_name and last_name to stdout
TypeError occurs when first_name is not a string
TypeError occurs when last_name is not a string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name to stdout.
    Args:
        first_name: str
        last_name: str
    Return: first_name, last_name
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
