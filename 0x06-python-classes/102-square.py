#!/usr/bin/python3
"""
This module illustrates the use of the Square class
defined in the 102-square module.
Calculates and displays the area of the square
using the private instance attribute: size.
Retrieves the private instance attribute: size
and sets it to a different value.
"""


class Square:
    """This class defines a square using private instance attribute: size."""
    def __init__(self, size=0):
        """Performs the instantiation of private instance attribute: size."""
        self.__size = size

    @property
    def size(self):
        """Retrieves the private instance attribute: size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance attribute: size to a different value."""
        try:
            self.__size = value
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise
        except ValueError:
            raise

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size

    def __eq__(self, val):
        return self.area() == val.area()

    def __lt__(self, val):
        return self.area() < val.area()

    def __gt__(self, val):
        return self.area() > val.area()

    def __ge__(self, val):
        return self.area() >= val.area()

    def __le__(self, val):
        return self.area() <= val.area()
