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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of Student instance.
        """
        if isinstance(attrs, list):
            res = {}
            for name in attrs:
                if isinstance(name, str) and hasattr(self, name):
                    res[name] = getattr(self, name)
            return res
        else:
            return self.__dict__
