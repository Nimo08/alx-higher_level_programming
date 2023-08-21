#!/usr/bin/python3
"""
Module creates instances of Rectangle class,
assigns width and height, then prints the id.
"""
from models.base import Base


class Rectangle(Base):
    """
    This class inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes private instance attributes and
        calls the super class with id.
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Retrieves value of width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width to different value.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves value of height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height to different value.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieves value of x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets x to different value.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves value of y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets y to different value.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates area of rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance with #.
        """
        for a in range(self.__x):
            for b in range(self.__y):
                if b != self.__y - 1:
                    print("")

        for i in range(self.__height):
            print(" " * self.__height, end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        Returns informal string representation.
        """
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.
        """
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
                if type(args[1]) != int:
                    raise TypeError("width must be an integer")
            if len(args) >= 3:
                self.__height = args[2]
                if type(args[2]) != int:
                    raise TypeError("height must be an integer")
            if len(args) >= 4:
                self.__x = args[3]
                if type(args[3]) != int:
                    raise TypeError("x must be an integer")
            if len(args) >= 5:
                self.__y = args[4]
                if type(args[4]) != int:
                    raise TypeError("y must be an integer")
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                    if type(value) != int:
                        raise TypeError("width must be an integer")
                elif key == 'height':
                    self.__height = value
                    if type(value) != int:
                        raise TypeError("height must be an integer")
                elif key == 'x':
                    self.__x = value
                    if type(value) != int:
                        raise TypeError("x must be an integer")
                elif key == 'y':
                    self.__y = value
                    if type(value) != int:
                        raise TypeError("y must be an integer")

    def to_dictionary(self):
        """
        Returns dictionary representation of a Rectangle.
        """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
