#!/usr/bin/python3
"""
Module illustrates the use of MagicClass class.
Calculates area and circumference of a circle.
"""


import math


class MagicClass:
    """This class defines a circle."""
    def __init__(self, radius=0):
        """Initializes the private instance attribute: radius."""
        if radius is not type(int):
            raise TypeError("radius must be a number")
        if radius is not type(float):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculates area."""
        return math.pi * self.__radius ** self.__radius

    def circumference(self):
        """Calculates circumference."""
        return 2 * math.pi * self.__radius
