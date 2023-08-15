#!/usr/bin/python3
"""
Module calls to_json function on
an instance of the Student class.
"""


class Student:
    """
    This class defines a student by public
    instance attributes: first_name, last_name
    and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes first_name, last_name and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of Student instance.
        """
        dict_1 = self.__dict__
        return dict_1
