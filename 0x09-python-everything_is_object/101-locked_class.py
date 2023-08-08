#!/usr/bin/python3
"""
LockedClass module tries assigning value
to instance attribute last_name and raises
an exception otherwise.
"""


class LockedClass:
    """This class prevents the user from dynamically creating new
    instance attributes, except if the new instance attribute
    is called first_name."""
    __slots__ = ['first_name']
