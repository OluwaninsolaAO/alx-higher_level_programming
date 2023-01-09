#!/usr/bin/python3
"""
A class named BaseGeometry -- it does stuff
"""


class BaseGeometry:
    """
    BaseGeometry -- does stuff

    @class methods
    area
    integer_validator
    """
    def area(self):
        """
        Raises a warning
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the variables ``name`` and ``values``
        passed to the method
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
