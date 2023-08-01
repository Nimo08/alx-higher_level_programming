#!/usr/bin/python3
"""
This module illustrates the use of the Square class
defined in the 6-square module.
It calculates and displays the area of the square
using the private instance attribute: size
It retrieves the private instance attribute: size
and sets it to a different value.
It creates a public instance method my_print()
which prints to the stdout, a square made of #.
It uses another private instance attribute:
position to print # to stdout.
"""


class Square:
    """This class defines a square using private instance attribute: size."""
    def __init__(self, size=0, position=(0, 0)):
        """This function performs the instantiation of
        private instance attribute: size."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """This function retrieves the private instance attribute: size."""
        return self.__size

    @size.setter
    def size(self, value):
        """This function sets the private instance attribute:
            size to a different value."""
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

    @property
    def position(self):
        """This function retrieves the private instance attribute: position."""
        return self.__position

    @position.setter
    def position(self, value):
        """This function sets the private instance attribute: size
        to a different value."""
        try:
            self.__position = value
            if not isinstance(value, tuple):
                raise TypeError("position must be a tuple of 2\
                        positive integers")
            if not isinstance(value[0], int) or not isinstance(value[1], int):
                raise TypeError("position must be a tuple of 2\
                        positive integers")
        except TypeError:
            raise

    def area(self):
        """This function calculates the area of the square
        using private instance attribute: size."""
        return self.__size * self.__size

    def my_print(self):
        """This function prints to the stdout, a square
        made of #."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            if self.__position[0] > 0:
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
