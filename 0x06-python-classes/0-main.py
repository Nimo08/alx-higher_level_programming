#!/usr/bin/python3
"""
Square module
This module illustrates the use of the Square class defined in the 0-square module.
It creates the Square object, prints the square type and displays its dictionary representation.

"""
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
