#!/usr/bin/python3
"""
Module contains an instance of the BaseGeometry class
and tries to print its area, otherwise raises an
exception message.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class inherits from BaseGeometry.
    Performs instantiation of private instance attributes:
    width and height.
    """
    def __init__(self, width, height):
        """
        Initializes private instance attributes: width and height.
        """
        BaseGeometry.integer_validator(self, width, height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates area.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return rectange description.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
