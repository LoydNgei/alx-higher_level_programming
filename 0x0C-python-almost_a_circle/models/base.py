#!/usr/bin/python3
"""Define a class Base"""


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
