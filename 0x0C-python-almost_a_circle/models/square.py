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

    def update(self, *args, **kwargs):
        """
        Updates the class instances' attributes with a
        no-keyword arguement, the position is as thus:
        - id
        - size: will be splitted into width and height
        - x
        - y
        """
        attr = len(args)
        if attr == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "size":
                        self.size = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

        if attr >= 1:
            self.id = args[0]
        if attr >= 2:
            self.size = args[1]
        if attr >= 3:
            self.x = args[2]
        if attr >= 4:
            self.y = args[3]

    def to_dictionary(self):
        """
        Returns a dictionary representation of the
        instance of the class.
        """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
