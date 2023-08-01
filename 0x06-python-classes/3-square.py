#!/usr/bin/python3
"""
This module illustrates the use of the Square class
defined in the 3-square module.
It calculates and displays the area of the square
using the private instance attribute: size.
"""


class Square:
    """This class defines a square using private instance attribute: size."""
    def __init__(self, size=0):
        """This function performs the instantiation of private instance
        attribute: size."""
        try:
            self.__size = size
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise
        except ValueError:
            raise

    def area(self):
        """This function calculates the area of the square
        using the private attribute: size."""
        return self.__size * self.__size
