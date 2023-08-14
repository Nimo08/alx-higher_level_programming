#!/usr/bin/python3
"""
Module contains MyList class that inherits from list.
Appends integers to my_list and prints the list,
but sorted in ascending order.
"""


class MyList(list):
    """
    This class inherits from the list class and
    contains public instance method print_sorted.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        Args:
            self: instance of class
        Return:
            sorted list
        """
        list_copy = self.copy()
        list_copy.sort()
        print(list_copy)
