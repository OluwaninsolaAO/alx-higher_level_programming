#!/usr/bin/python3
"""
A simple programme that returns the dictionary description
with a simple python data structure for JSON serialization
of an object.
"""


def class_to_json(obj):
    """
    ``obj`` being an instance of a class,
    the attributes of ``obj`` can be accessed
    using ``__dict__``.
    Funtion returns a dictionary returned from
    accessing the attributes of ``obj``.
    """
    return obj.__dict__
