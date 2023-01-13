#!/usr/bin/python3
"""Define a class and inherited class-checking function"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class
    (directly or indirectly) from the specified class otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
