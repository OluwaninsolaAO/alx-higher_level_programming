#!/usr/bin/python3
"""
A simple python programme that repeat the names
passed down unto it.
"""


def say_my_name(first_name, last_name=""):
    """
    This programme takes two arguements
    ``first_name``: must be a string (required)
    ``last_name``: String (not required)
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
