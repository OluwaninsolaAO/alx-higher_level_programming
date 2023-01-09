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

    def __init__(self, width, height):
        """
        init method -- called on creation of new member
        the class
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
