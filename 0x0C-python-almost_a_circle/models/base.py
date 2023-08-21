#!/usr/bin/python3
"""
Module creates instances of Base class
and prints the value stored in the instance attribute: id.
"""


import json


class Base:
    """
    This class defines a public instance attribute: __nb_objects
    and performs instantiation for public instance attribute: id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes id if it is not None, otherwise increments it.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        filename = type(list_objs[0]).__name__ + ".json"
        json_list = [i.to_dictionary() for i in list_objs]
        json_str = cls.to_json_string(json_list)
        with open(filename, 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            obj = Rectangle(2, 3)
        elif cls.__name__ == "Square":
            obj = Square(2)
        else:
            obj = None
        if obj:
            obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        from os.path import exists
        instance_list = []
        filename = cls.__name__ + ".json"
        if exists(filename):
            with open(filename, 'r') as f:
                file = f.read()
                if len(file) > 0:
                    instance_list = cls.from_json_string(file)
        instance_list = [cls.create(**instance) for instance in instance_list]
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes in CSV.
        """
        import csv
        filename = type(list_objs[0]).__name__ + ".csv"
        csv_list = [i.to_dictionary() for i in list_objs]
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_list)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize in CSV.
        """
        import csv
        from os.path import exists
        instance_list = []
        filename = cls.__name__ + ".csv"
        if exists(filename):
            with open(filename, 'r') as f:
                csvreader = csv.reader(f)
        instance_list = [cls.create(**instance) for instance in instance_list]
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.
        """
        import turtle
        list_rectangles = turtle.Turtle()
        turtle.fillcolor("DarkSalmon")
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(120)
            turtle.left(120)
        turtle.end_fill()
        turtle.fillcolor("PeachPuff2")
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(120)
            turtle.right(90)
        turtle.end_fill()
        list_squares = turtle.Turtle()
        turtle.fillcolor("LemonChiffon2")
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()
        turtle.done()
