#!/usr/bin/python3
"""
This module contains a definition of a class Rectangle
that inherits from Class Base, Rectangle will intially
be defined to have the following lists of attributes:
    - width: being the width of the class
    - height: being the height of the class
    - x: x value
    - y: y value
    - id: instance id.
Each of these variables with its own getter and setter
and couple of private attributes to protect some of the
attributes.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class - ^^^
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle Class constructor, handling attributes
        creation and call on super class Base.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.__y = value

