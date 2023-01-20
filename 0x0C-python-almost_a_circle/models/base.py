#!/usr/python3
"""Define a class Base"""


__nb_object = 0


def __init__(self, id=None):
    """Initialize the class constructor"""
    if id is not None:
        self.id = id
    else:
        Base.__nb_object += 1
        self.id = Base.__nb_objects
