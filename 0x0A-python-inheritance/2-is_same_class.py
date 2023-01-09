#!/usr/bin/python3
"""
A function that compares a object with a class
"""


def is_same_class(obj, a_class):
    """
    Returns true if obj is an instance
    of a_class and false if otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
