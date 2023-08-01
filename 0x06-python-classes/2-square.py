#!/usr/bin/python3
"""
Square module
This module illustrates the use of the Square class
defined in the 0-square module.
It creates the Square object, prints the square type
and displays its dictionary representation.
"""


class Square:
    """This class defines a square using private instance attribute: size."""
    def __init__(self, size=0):
        """This function performs the instantiation of private instance
        attribute: size with no type or value verification."""
        try:
            self._Square__size = size
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise
        except ValueError:
            raise
