#!/usr/bin/python3
"""Function adds new attribute to an object if possible"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible

    Args:
        obj (any): The object to add attribute to
        att (str): The name of thee attribute to add to obj
        value (any): The value of att
    Raises:
        TypeError: If the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("cant add new attribute")
    setattr(obj, att, value)
