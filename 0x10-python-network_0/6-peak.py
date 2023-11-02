#!/usr/bin/python3
"""
Module calls the find_peak function.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    for index, num in enumerate(list_of_integers):
        if num >= list_of_integers[index - 1] and\
           num >= list_of_integers[index + 1]:
            return num
