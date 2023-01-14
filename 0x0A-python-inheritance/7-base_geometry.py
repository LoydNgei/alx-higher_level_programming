#!/usr/bin/python3
"""Define a class BaseGeometry with 2 public instances"""


class BaseGeometry:
    """Represents the class BaseGeometry"""

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public class instance that validates value
        Args:
            name (str) = assume is always a string
            value (int) = The argument to be validated

        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less or equal to 0
            """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
