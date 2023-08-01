#!/usr/bin/python3
"""
This module illustrates the use of the Square class
defined in the 101-square module.
Calculates and displays the area of the square
Retrieves the private instance attribute: size
and sets it to a different value.
Prints to the stdout, a square made of #.
Uses another private instance attribute:
position to print # to stdout.
"""


class Square:
    """This class defines a square using private instance attribute: size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initiliaze square with a size and position."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or\
                not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Retrieves the private instance attribute: size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance attribute:
            size to a different value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the private instance attribute: position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the private instance attribute: size
        to a different value."""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints to the stdout, a square made of #."""
        if self.__size == 0:
            print("")
            return
        for a in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            if self.__position[0] >= 0:
                print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        string = ""
        if self.__size == 0:
            return ""
        for a in range(self.__position[1]):
            string += "\n"
        for i in range(self.__size):
            if self.__position[0] >= 0:
                string += " " * self.__position[0]
            for j in range(self.__size):
                string += "#"
            if i != self.__size - 1:
                string += "\n"
        return string
