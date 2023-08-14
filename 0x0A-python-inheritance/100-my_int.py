#!/usr/bin/python3
"""
MyInt module prints my_i instance
"""


class MyInt(int):
    """
    This class inherits from int.
    """
    def __init__(self, value):
        """
        Initializes instance attribute value.
        """
        self.value = value

    def __eq__(self, other):
        """
        Reverses the eq method.
        """
        return self.value != other

    def __ne__(self, other):
        """
        Reverses the ne method.
        """
        return self.value == other
