#!/usr/bin/python3
"""
Module contains Rectangle function
Rectangle function: defines a rectangle using
private instance attributes: width and height
Calculates the area and perimeter of rectangle
Returns informal string representation of rectangle
Returns official string representation of rectangle
Deletes an instance of Rectangle
Returns the biggest rectangle based on the area
Print the rectangle with the character(s) stored in print_symbol
Returns a new Rectangle instance
TypeError: width or height is not an integer
ValueError: width or height is less than 0
"""


class Rectangle:
    "Defines a rectangle"
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns informal string representation of rectangle"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            print("")
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i != self.__height - 1 or i != self.__width:
                string += "\n"
        return string

    def __repr__(self):
        """Returns official string representation of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes an instance of Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """Print the rectangle with the character(s) stored in print_symbol"""
        symbol = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                symbol += str(self.print_symbol)
            if i != self.__height - 1:
                symbol += "\n"
        return symbol

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        if rect_2.area() >= rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance"""
        return cls(size, size)
