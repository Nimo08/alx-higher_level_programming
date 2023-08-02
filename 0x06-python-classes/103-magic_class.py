#!/usr/bin/python3
import math
class MagicClass:
    def __init__(self, radius=0):
        if radius is not type(int):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        return math.pi * self.__radius ** self.__radius

    def circumference(self):
        return 2 * math.pi * self.__radius
