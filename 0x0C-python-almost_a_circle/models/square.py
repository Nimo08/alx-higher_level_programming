#!/usr/bin/python3
"""
Module creates instances of Square class,
prints the instance and the area.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits from Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes instance attributes: size, x, y and id.
        """
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieves value of size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets size to different value.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def __str__(self):
        """
        Returns informal string representation.
        """
        return "[Square] ({}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Assigns attributes to arguments.
        """
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                if type(args[1]) != int:
                    raise TypeError("width must be an integer")
            if len(args) >= 3:
                self.x = args[2]
                if type(args[2]) != int:
                    raise TypeError("x must be an integer")
            if len(args) >= 4:
                self.y = args[3]
                if type(args[3]) != int:
                    raise TypeError("y must be an integer")

        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    if type(value) != int:
                        raise TypeError("width must be an integer")
                elif key == 'x':
                    self.x = value
                    if type(value) != int:
                        raise TypeError("x must be an integer")
                elif key == 'y':
                    self.y = value
                    if type(value) != int:
                        raise TypeError("y must be an integer")

    def to_dictionary(self):
        """
        Returns dictionary representation of a Square.
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
