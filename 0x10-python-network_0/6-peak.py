#!/usr/bin/python3
"""
Module calls the find_peak function.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    low = 0
    high = len(list_of_integers)

    while low < high:
        mid = (low + high) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1])\
                and (mid == high - 1 or
                     list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid
        else:
            low = mid + 1
    return None
