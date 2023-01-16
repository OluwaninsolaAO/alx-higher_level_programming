#!/usr/bin/python3
"""
This module contains a class definition Base with the
following attributes:
    - private class attribute __nb_objects = 0 for a
    start.
"""
import json
import csv
import turtle


class Base:
    """
    ``Base`` will have a class attribute ``__nb_objects``
    with its constructor taking the arguement ``id``
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for the class Base.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of
        ``list_dictionaries``.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of
        ``list_objs`` to a file:
        - ``list_objs`` is a list if instances who inherits of Base
        - The file name will be <class name>.json
        - Overwrite the file if it already exists.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as fi:
            if list_objs is None:
                fi.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                fi.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns python data structure of ``json_string`` arguement
        passed into the method:
        - ``json_string`` being a json string representation
        of dictionaries.
        - if ``json_string`` is None or empty, the method returns
        an empty list otherwise, return the list represented by
        ``json_string``.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes of the instance
        set, ``dictionary`` is a dictionary describing the
        attributes of the instance.
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as fi:
                json_str = Base.from_json_string(fi.read())

            return_list = []
            for item in json_str:
                instance = cls.create(**item)
                return_list.append(instance)
            return return_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.
        ``list_objs`` being a list of obj instance of the class.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="", encoding="utf-8") as fi:
            if list_objs is None or list_objs == []:
                fi.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(fi, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="", encoding="utf-8") as fi:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(fi, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle module:
        - ``list_rectangles`` -  A list of Rectangle objects to draw.
        - ``list_squares`` - A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
