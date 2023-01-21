#!/usr/bin/python3
"""Define a class Base"""
import json
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
        with open(filename, "w") as jsonfile:
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

        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns  an instance with all attributes already set

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
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
