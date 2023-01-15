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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the object.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints to the standard output a representation of
        the instance with a ``#`` character.
        """
        for y in range(self.y):
            print("")
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        Returns a string representation of
        Rectangle
        """
        __str = "[Rectangle] ({}) {}/{} - {}/{}"
        return __str.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates the class instances' attributes with a
        no-keyword arguement, the position is as thus:
        - id
        - width
        - height
        - x
        - y
        """
        attr = len(args)
        if attr == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

        if attr >= 1:
            self.id = args[0]
        if attr >= 2:
            self.width = args[1]
        if attr >= 3:
            self.height = args[2]
        if attr >= 4:
            self.x = args[3]
        if attr >= 5:
            self.y = args[4]
