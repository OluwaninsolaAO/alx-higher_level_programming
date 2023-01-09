#!/usr/bin/python3
"""
A simple class that inherits from another
class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class, being a sub-class or a child-class
    of BaseGeomertr
    """
    _width = int()
    _height = int()

    def __init__(self, width, height):
        """
        init method -- called on creation of new member
        the class
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
