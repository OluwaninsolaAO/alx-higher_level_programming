#!/usr/bin/python3
"""
This module contains a definition of a class Square
that inherits from Rectangle calss, unlike Rectangle
that was has width and height as part of its contructor
variables, Square will be using size since all sides
of a sqaure are all equal. The following describes the
initial attributes of the Square Class:
    - size: being the size of the sides
    - x: x value
    - y: y value
    - id: instance id.
Each of these variables with its own getter and
setter (from parent class) and couple of private
attributes.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class - ^^^
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class contrustor, handling attributes
        creation and call on super class Rectangle.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get or set the value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of Square
        """
        __str = "[Square] ({}) {}/{} - {}"
        return __str.format(self.id, self.x, self.y, self.width)
