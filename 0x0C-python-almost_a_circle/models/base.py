#!/usr/bin/python3
"""Define a class Base"""
import json
import os
import csv
import turtle


class Base:
    """Represents the base model
    Attributes:
        __nb_objects (int): The number of instantiated Bases
        """
    __nb_object = 0

    def __init__(self, id=None):
        """Initialize the class constructor
        Args:
           id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON str representation of list_dictionaries

        Args:
            list_dictionaries: List of dictionaries
        """
        if (list_dictionaries is None or list_dictionaries == []):
            return "[]"
        return json.dump(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file
        Args:
            list_objs: List of instances who inherit of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON str representationjson_string
        Args:
            json_string: is a str representing a list of dictionaries
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns  an instance with all attributes already set

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize
        """
        if cls.__name__ == "Rectangle":
            new = cls(3, 6)
        else:
            new = cls(3)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Function that saves list of objects to a CSV file

        Args:
            list_objs (list): list of instances
        """
        file_name = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns the list of instances depending on class from a CSV
                Reads from `<cls.__name__>.csv`
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=field_names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangle, list_squares):
        """Opens a window and draws all the rectangle and squares"""
        my_turtle = turtle.Turtle()
        my_turtle.shape("turtle")
        my_turtle.pensize(2)

        for rec in list_rectangles:
            if rec.x > 0 and rec.y > 0:
                my_turtle.penup()
                my_turtle.goto(rec.x, rec.y)
                my_turtle.pendown()
            else:
                my_turtle.penup()
                my_turtle.home()
                my_turtle.pendown()
            my_turtle.pencolor("green")
            for i in range(2):
                my_turtle.fd(rec.width)
                my_turtle.rt(90)
                my_turtle.fd(rec.height)
                my_turtle.rt(90)
        for s in list_squares:
            if s.x > 0 and s.y > 0:
                my_turtle.penup()
                my_turtle.goto(s.x, s.y)
                my_turtle.pendown()
            else:
                my_turtle.penup()
                my_turtle.home()
                my_turtle.pendown()
            my_turtle.pencolor("red")
            for i in range(4):
                my_turtle.fd(s.size)
                my_turtle.rt(90)
                my_turtle.ht()
