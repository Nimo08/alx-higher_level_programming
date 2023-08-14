#!/usr/bin/python3
"""
Module contains Square class
inherited from Rectangle class
Prints area
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class inherits from Rectangle class.
    Performs instantiation of private instance attribute: size.
    """
    def __init__(self, size):
        """
        Initialiazes private instance attribute: size.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates area.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns informal string representation of an object.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
