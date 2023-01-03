#!/usr/bin/python3
"""
A simple locked class using __slots__
Usage of __slots__ reduces the wastage of space and
speed up the program by allocating space for a fixed
amount of attributes.

If __slots__ is present in any class objects, any
variable names not declared in the list will not be
dynamically created.
"""


class LockedClass():
    """
    The locked class will be using __slots__
    """
    __slots__ = ['first_name']
