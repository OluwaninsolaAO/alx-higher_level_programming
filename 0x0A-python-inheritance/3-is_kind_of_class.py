#!/usr/bin/python3
"""
A function that checks if an object is an instance of
a class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true if is an instance or False
    if otherwise
    """
    return isinstance(obj, a_class)
