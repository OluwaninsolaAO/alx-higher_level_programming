#!/usr/bin/python3
"""A functions that checks is a class is a subclass
of another class
"""


def inherits_from(obj, a_class):
    """
    Returns True if ``obj`` is a subclass
    of ``a_class`` or False if otherwise
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
