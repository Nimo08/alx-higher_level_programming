#!/usr/bin/python3
"""
Module contains Rectangle function
Rectangle function: defines a rectangle using
private instance attributes: width and height
TypeError: width or height is not an integer
ValueError: width or height is less than 0
"""


class Rectangle:
    "Defines a rectangle"
    def __init__(self, width=0, height=0):
        """
        Initializes private instance attributes: width and height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Retrieves the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Changes the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Retrieves the value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Changes the value of width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
