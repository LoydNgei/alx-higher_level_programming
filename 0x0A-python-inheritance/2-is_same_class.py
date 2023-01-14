#!/usr/bin/python3
"""Define a class-checking function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class
   Args:
     obj: The object to check
     a_class: The class to match the type of obj to
   Returns:
       True - if obj is exactly an instance of obj to
       False - Otherwise
    """

    if type(obj) == a_class:
        return True
    else:
        return False
