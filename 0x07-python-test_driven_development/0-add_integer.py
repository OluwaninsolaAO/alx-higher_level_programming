#!/usr/bin/python3
"""Simple addition of two numbers --
of type int or float"""


def add_integer(a, b=98):
    """Returns a + b"""

    types = [int, float]

    if type(a) not in types:
        raise TypeError("a must be an integer")
    if type(b) not in types:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
