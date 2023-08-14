#!/usr/bin/python3
"""
Module contains an instance of the BaseGeometry class
and tries to print its area, otherwise raises an
exception message.
"""


class BaseGeometry:
    """
    This class contains a public instance method: area.
    """
    def area(self):
        """
        Raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
